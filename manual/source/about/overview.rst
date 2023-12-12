A BGP ‘Echo’ Application
~~~~~~~~~~~~~~~~~~~~~~~~

So, from the previous chapter we learned that a BGP application does not have
to do everything a BGP speaker does. The only must-have seems to be the
ability to decipher BGP packets. For an application to do something useful it
also probably must be able to output something. The minimal useful BGP
application that we can come up with, then, looks something like this:

Fig.1 BGP ‘Echo’ Application

BGP packets ingress -> BGP packets egress

If our ‘Echo’ application was a UNIX utility, we would probably assume the
default ingress would be STDIN and the default egress would be STDOUT. That
would give us quite a bit of flexibility and extensibility: the user would be
able to pipe the output of some other program into ours and likewise they
could transform the output by piping into another program. There is
significant drawback tough: our pipes would only ever be useful if our ‘Echo’
application and the programs at the other end of the pipe would use the same
encoding. We could use, for example, the ``mrt`` (:RFC:`6396`) format. Also,
if we really want to output to STDOUT, we probably want to use a
human-readable serialisation format there.

What if we could make our ‘Echo’ application a bit more flexible by creating
an input ’thing’ that could acquire BGP packets from different types of inputs
and then transform that into BGP packets. If we do the same thing in reverse
on the output side, it would something like this:

Fig.2 BGP ‘Echo’ Application 2

input from (socket, ``mrt`` file, stdin) -> BGP packets -> output to (socket,
``mrt`` file, stdout)

Neat! Now we can take input from various sources and pipe into another
program, dump it to a file, or to stdout. Our application is still a bit
simplistic, though, if you consider the socket input and output, for example.
How would BGP packets appear on the socket? That would require a live BGP
session on that socket at least. Also, an ``mrt`` file input resembles BGP
packets, they are not the same, we would still need to transform the input
into actual BGP packets that our application can internally handle.

Why don’t we create a thing that can setup a BGP session on a socket and can
then take BGP input from that session hand it to the rest of our application?
Let’s do that, and, while we’re at it, we can also create a similar thing on
the output side that can handle BGP sessions, or maybe open an output file, or
something else that needs state. Since the format of the input and the output
can differ, and both may not be actual BGP packets at all, and bot the input
and the output handler have their own transform mechanisms, we are probably
better off creating an internal BGP representation for our application. 

Fig.3 BGP ‘Echo’ Application 3

input type handler -> into BGP transformer for input type -> internal BGP
representation -> into output format transformer -> output type handler

We have now two ‘things’ on each end in our application, but we have a
multitude of type of ‘things’, one type per format and input source
combination that we would like to support. Also, in our ‘thing’ types the
handler and the transformer are tightly coupled, so this would be a good time
to start calling our handler and transformer ‘things’ `units`. We now have two
units: a `ingress` unit that combines the input handler and its transformer
and a `egress` unit that combines the output handler and its transformer.

Fig 4. BGP Echo Units Application

ingress unit -> egress unit

We can now create different ingress and egress units for all kinds of sources.
Let’s say that we create an ingress unit for a BGP session. BGP sessions are
opened over TCP, so let’s call our unit, ``bgp-tcp-in``. We could also have a
unit ``mrt-file-in`` for ``mrt`` files, and so on.

Almost done. We still have one problem, our BGP input contains lots of
messages that we don’t care about, let’s say for now everything that is not a
BGP UPDATE message. We don’t want any other BGP messages in our output. We
need to filter them out. So, in the middle let’s create a filter called
``update-filter``. That filter would simply take as its input an internal
representation of a BGP packet and take a decision to let it pass or not,
‘Accept’ or ‘Reject’, based on what kind of BGP packet flows through it.

Fig. 5 Echo application

ingress unit -> update-filter -> egress unit

This is the pipeline of our minimal viable BGP ‘Echo’ application. And with
that we have been introduced to two elemental parts of Rotonda: `Units` and
`Pipelines`.

Beyond the ‘Echo’ Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s take a closer look at our filter. We have a filtering function that is
hard-coded to only ‘Accept’ BGP UPDATE messages. That sounds a bit ..
arbitrary. Wouldn’t it be nicer to let our users decide what they want to
filter on? Then our filter could also be unit type! Let’s go with that plan
and assume we’re going to offer ours users a generic filter that can contain
some logic that they define to create the filtering decision. This filter
would still take as its input our internal BGP representation and its output
would still be the `Accept` or `Reject` value, the filtering decision. So, now
we can offer a smarter `Echo` application, with a programmable filter, let’s
call it the `FilteredEcho` application.

Fig. 5 The ‘FilteredEcho’ application

(configurable) ingress unit -> (programmable) filter unit -> (configurable) egress unit

Storing Data in the Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our ‘FilteredEcho’ application slices, it dices, but as it goes with
successful things, our users want more. Our users want to be able inspect the
*current* state of a prefix that was received at one point in one or more BGP
packets, they want to learn if it was announced with that community, not seen
at all, or withdrawn. So how do we go about this? We could of course say, we
gave you a BGP echo application, if you want that, you should accumulate that
state yourself as a consumer of our stream. But we are not like that, we will
help our users out, so let’s invent something for them. 

As we saw, the Routing Information Base (RIB) is one of the fundamental
elements of BGP. Could we reuse that for our ‘StatefulFilteredEcho’
application? Turns out we can. If we put a RIB to the right of our filter and
assume that that RIB will be able to store routes that got the ‘accept’ for
our filter, then we have the desired state.

Fig. 6 The preliminary `StatefulFilteredEcho` application

ingress unit -> filter unit -> RIB -> egress unit

Now we have the state we want, but if we assume that our filter is unchanged
we have way too *much* state, we’re storing all the prefixes, because all the
messages get through and will be ‘disassembled’ into route announcements or
withdrawals. So if we assume that our filter could inspect the route
announcements and withdrawals in the UPDATE packet, we could have it accept
only the packets that contain the community that our users are interested in.
The store would store all prefixes that have the community attached, and,
assuming the RIB would have the logic to handle announcements and withdrawals
we would have the desired state captured in our pipeline. After storing the
routes that flow through the filter it will pass the routes on in our
pipeline, as routes. As a matter of fact, we have changed the output type of
our filter! We ’disassembled’ the packet, so the output type of our filter is
already a bunch of routes, instead of the packet we had earlier on.

Fig 7. The `StatefulFilteredEcho` Application with types

|                                                  query prefix                 
|                                                       │                   
|                                                       ▼                   
| ingress unit<BGP p> ─▶ filter unit<routes> ─▶ RIB<routes> ─▶ egress unit
|                                                       │                   
|                                                       ▼                   
|                                                  query result             

Our RIB now contains everything we need, but we’re not done yet, because our
users need a way to get the actual state of their prefixes out. Up until this
point we used our RIB basically the way it was defined in :RFC:`4271`, but now
we going to extend it a bit: we’re going to add query capabilities to our RIB.
So now we have a west-to-east pipeline with our BGP data and one
north-to-south flow, where are users can provide a query for a prefix on the
north side of the RIB, and get a result out at the south side of the same RIB.

Our filter is fairly tightly coupled with the RIB now, the output type of the
filter should exactly fit the type that the RIB stores, so before we declare
our RIB also a unit type, we should consider this. So let’s make a RIB unit
that simply includes a ‘filter’ to express that. Our RIB **unit** would look
like this:

Fig. 8 RIB Unit

|                   query prefix                 
|                        │                   
|                        ▼                   
| filter<routes> ─▶ RIB<routes>
|                        │
|                         ▼                   
|                    query result

Transforming Data
~~~~~~~~~~~~~~~~~

Our users are happy now, but they think they would be even more happy, if the
output from their queries would only show its current status (never seen,
announced, or withdrawn) and the AS path. The rest doesn’t interest them, and
they think it’s a waste of space. Hard to disagree there, nobody wants to
waste space, right? But what can we do, our RIB can only store complete
routes, so that would be something like the tuple ``(prefix, status,
path_attributes)``, and they want ``(prefix, status, as_path)``. Note that we
can omit the actual community, because it’s implied in the existence of the
tuple in our RIB.

In line with :RFC:`4271` we defined our RIB to store routes, with the prefix
as the key. But what if we defined our RIB to be able to store an arbitrary
type, let’s call it `metadata`. Our tuples that we store in our RIB would then
look like: ``(prefix, metadata)``. Since ``metadata`` is an arbitrary type,
that in itself could be a tuple ``(status, as_path)`` for example.

Since the output type of the filter must be the storage type of the store our
filter in the RIB should output the same type, ``(prefix, metadata)``. But
that is a problem! Remember, filters cannot change the output, as a matter of
fact, they don’t even output anything else but the filtering decision. For
that we will have to invent another type of unit: the ``FilterMap``. A
``FilterMap`` can both make filtering decision *and* transform the payload it
receives and output the transformed payload. A `FilterMap` acts also as a
normal filter if the input payload and the output payload are the same.

So let’s change our RIB unit, and replace the ``Filter`` with a ``FilterMap``,
and integrate it into our new, all-singing and dancing `StatusAsPathStorage`
application based on our `StatefulFilteredEcho`, but with significant changes.

Fig. 9 ‘StatusAsPathStorage’ Application

|                                       query prefix              
|                                            │                   
|                                            ▼              
| ingress unit<BGP p> ─▶ filtermap<T> ─▶  RIB<T> ─▶ egress<T> unit
|                                            │                   
|                                            ▼                   
|                                      query result<T>

where T: (status, as_path)

Besides using our new RIB type, we’ve changed the input type to that RIB to
``(status, as_path)``, and therefore it also outputs that same type. The user
can query the application, and will also get instances of that same type out.
Finally, to the east we also get instances out of that type.

Egressing other data
~~~~~~~~~~~~~~~~~~~~

Still our users are not satisfied! In spite of their latest BGP application
being able to open BGP connections, ingress, transform and store the relevant
data, while making it queryable, they want the east egress unit to output
*all* announcements and withdrawals from the UPDATE messages it receives on
the ingress unit, while keeping all other functionality. Ok, let’s present the
solution without further ado:

Fig. 10 ‘StatusAsPathStorage2’ Application

| ingress<BGP packet> unit ─▶ filter<routes> unit ┌─────▶ egress<routes> | unit
|                                                 │                     
|                                                 ▼                     
|                                     RIB<(status, as_path)> unit

We have a filter *unit* that sits before the egress and the RIB unit. That
filter unit filters to let only UPDATE messages flow through. From there it
*splits* into a flow direct at the RIB, which in its latest incarnation has a
filtermap of its own, that filters on the community our users want and
transforms the routes into ``(prefix, (status, as_path))`` pairs and stores
those into the RIB. The RIB can be queried by our users. The other branch
flows to the east from the filter unit as routes, where they can be picked by
our users at the egress unit.

A Virtual RIB
~~~~~~~~~~~~~

Ok, now our users have *one* last request: they want to be able to query the
current status and all attributes for all the routes that come out of the
UPDATE messages. Simultaneously they want to be able to query the RIB for
prefixes with the particular community and retrieve their status and as_path.
On the east they want the routes from the UPDATE messages echoed, both
announcements and withdrawals.

Now, we could solve this by creating a pipeline that contains two RIBs, one
for all the routes and one for the routes containing the particular community.
That would waste space, though, since we would store the routes with the
community *twice*, one time in each RIB. A better pipeline plan would include
something we call a ‘Virtual RIB’, that’s a RIB that does not store anything
itself, but instead goes back to the closest RIB on its west-side and filter
on prefixes present in that RIB. 

Our whole pipeline plan would look like:

Fig. 11 ‘VirtualRIB1’ Application

| ingress<BGP packet> unit ─▶ pRIB<routes> unit ┌─────▶ egress<routes> unit
|                                               │                     
|                                               ▼                     
|                                 vRIB<(status, as_path)> unit

We have now called the RIB we already had, `pRIB’ as an abbreviation for
`physical RIB` to set it apart from the virtual RIB, ‘vRIB’. Our vRIB here is
dependent on the pRIB from which routes flow come flowing in. It adds
additional filtering and transforms the incoming routes, while being fully
queryable, like the physical RIB.

Wrapping it up for now
~~~~~~~~~~~~~~~~~~~~~~

And this is some of the stuff users will be able to construct with Rotonda.
There are more types of units that we haven’t discussed here, we didn’t
mention ``Roto`` yet, the language that allows users to program Filter(Maps).
The rest of this documentation is about those.

A Word about the Minimal Viable Product (‘MVP’)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not everything described above is possible with the first release, the
“Minimum Viable Product”, of Rotonda, partly because some details are still
lacking in the Rotonda code, partly because not all configuration options are
there yet. All the unit types, as well as the BMP and BGP ingress connectors
do exist though.

In the first release, Rotonda has a fixed default pipeline, that is described
in detail in this documentation <<<here>>> TODO. That configuration can be
changed however to resemble the pipelines mentioned, but they are largely
untested, so at this point we don’t know if they actually work.

Where to go from here?
~~~~~~~~~~~~~~~~~~~~~~

When you’ve read of all this introduction and you like what you’ve read, you
may want to actually install Rotonda. See those instructions <<<here>>> TODO.

We have a practical <<quicktour>> for you, that talks through a working setup
and suggesting some modifications you can try and see their effect.

Then, we have a more in-depth chapter on <<configuring Rotonda>>.

Finally, we have the full reference of the `Roto` filter (and query) language,
and the full description of all the units.
