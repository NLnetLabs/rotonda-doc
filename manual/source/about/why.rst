On speaking BGP
---------------

Central to Rotonda is the observation that there is no one-size-fits-all
application for a network's BGP routing needs any more. As networks are
growing, so is their complexity, and as a consequence, BGP is being used in
more places in the network, and it has turned into a generic container for
information about network nodes, increasing its complexity. Pressure on BGP to
offer better security further increased the complexity of BGP itself and its
deployments.

By now, the notion of a "BGP speaker" (the wording of :RFC:`4271`) with a
fixed set of "Routing Information Bases" (RIBs) with prescribed behaviour is
only one of many different `BGP functions`, as we would like to call them,
that we can identify in a network. Rotonda aims to provide users with the
building blocks to create their own application optimized for any of these BGP
functions.

BGP Functions
-------------

So, what are these BGP functions anyway? The way we would like to describe them
is "a specialised task within a network relying on BGP, that requires a
subset of BGP's features". Often, this task is performed by a node in the
network.

BGP's Features
--------------

Before we delve deeper into BGP functions, let's first establish what we mean
with BGP's features, by posing the question: "What are the
requirements for a fully-fledged BGP speaker?". :RFC:`4271` and its updates
describes BGP consisting of three components: the BGP packet format, the BGP
state machine, and the Routing Information Base.

The specific required interaction of these components describe BGP's features,
they boil down to:

"Listening" or "Passively speaking" BGP
    - parsing BGP packets
    - opening and maintaining sessions with the BGP state machine

    This is the least amount of work a BGP function would need to do in order
    to be accepted as a functioning part of a network routed with BGP. Note
    that both the terms "listening" and "passively speaking" are colloquial,
    i.e. not mentioned anywhere in the RFCs.

"Keeping State in RIBs"
    - storing incoming routes in "adj-RIB-in", "loc-RIB" and "adj-RIB-out"

    In order for a BGP function to conform to an IETF standards-compliant "BGP
    speaker" it would have to feature these RIBs, at least, "logically"
    (again, you guessed it, :RFC:`4271`).

"Speaking" BGP
    - performing best-path selection
    - propagating routes to peers

    Based on the contents of its RIB-ins and its configured policies, it should
    implement the best-path selection rules from :RFC:`4271` and propagate the
    selected routes to its peers.

These are the features which, if implemented correctly, allow for an
application to be an IETF standards compliant "BGP Speaker". As we stated
before, though, a BGP function does not have to implement all of them to
fulfil their function. Even more so, for them to function correctly, they
don't have to be standards-compliant for all these features.

It would be nice if the first feature, "Passively speaking", is implemented
completely standards-compliant, since it would hamper the interaction with
other BGP speakers if it wasn't. Since it is valid for a BGP speaker to have a
(local) policy in place that discards all routes to "adj-RIB-out", a BGP
speaker that never propagates any route could still be standards-compliant.
From that, it follows that such a BGP speaker will not have to engage in
best-path selection, and in turn, it wouldn't have to do any state-keeping.
Strictly speaking, it would at that point not be standards-compliant any more,
but there would be no way for an outside observer to establish its
non-compliance. We shall see that many a BGP function does indeed not require
one or both of the "Keeping state" or "Speaking BGP" features, hence the word
"subset" in our definition.

Route Server
------------

A Route Server (as mentioned in :RFC:`7947`) would be a clear-cut example of a BGP
function. A Route Server requires the "Speaking BGP" feature of the BGP protocol
and the BGP state machine, but it does not require the best-path selection
mechanism, at least not in the form mentioned in :RFC:`4271` and its updates.

Route Reflector
---------------

Likewise, a Route Reflector (:RFC:`4456`) serves a specific function in an iBGP
network. Again, it requires the "Speaking BGP" feature of the BGP protocol, but
it doesn't have to engage necessarily in best-path selection. Very simple
Route Reflectors would not have a need for RIBs, they would just reflect the
announcements and withdrawals they receive to their iBGP peers.

Route Collector
---------------

A Route Collector is, broadly speaking, a device that passively engages in BGP
sessions with the purpose of storing the learned routes together with
meta-data about the whereabouts of these routes. Some of the purposes of
storing these routes would be troubleshooting, and (longitudinal) analysis.

"Passively engages" may mean that the collector wil connect over BMP (BGP
Monitoring Protocol), out-of-band, with one or more BGP routers. In this case
the collector, called a "BMP Station" (:RFC:`7854`), will **not** be a node in the
BGP network. It will only require the packet parsing features of BGP in order
to be able to extract the routes, and to be able to gather metadata. 

More commonly, though, Route Collectors **are** a node in the BGP network and
the collector tries to "Passively Speak". As we saw, though, a passive speaker
will have to engage in a minimum of speaking BGP. A Route Collector must never
engage in best-path selection, or propagate routes to its peers whatsoever.
Therefore, Route Collectors have no need for keeping state in RIBs as
described in :RFC:`4271`. Indeed, Route Collectors may entirely forego having
RIBs, since they can be synthesised later from the stored routes and meta-data
if need be.

Route Monitor
-------------

A Route Monitor is like a Route Collector in that it engages passively with
BGP speakers through BMP or "Passively speaking". However, instead of or in
addition to storing, it will send signals to other systems and/or applications
based on specific user-defined events or combinations of (accumulated) events
occurring in the observed BGP network. Some purposes would be troubleshooting,
post-mortem analysis and anomaly detection.

Other Functions
---------------

There are other numerous BGP functions that already exist in some shape or
form or that could be extracted from current practices, to name just a few:

- Off-line Looking Glass
- Route Provisioning
- Route Policy Engine
- RPKI injection Filter
- Edge Sanitation Filter ("Edge Lord")
- Route Optimizer

From BGP Function to BGP Application
------------------------------------

All of the BGP functions mentioned here exist today, as hardware devices, or
as software applications, be it open-source or proprietary. Many of these
applications, though, were not intended to be used for these BGP functions,
e.g. requiring patching, and/or requiring a multitude of applications, glued
together with ad-hoc code.

Rotonda aims to alleviate this by offering the user the tools, a framework if
you will, that allows users to build their own *BGP application* that may
perform one or multiple, combined BGP functions, without aforementioned
problems.

Secondly, Rotonda wants to be a tool that you can easily spin up to collect,
experiment with and analyze BGP (and related) data.

Thirdly, Rotonda aspires to lower the barrier to implement new, experimental
BGP (and routing) features, not only by offering this already-mentioned
framework, but also by allowing plugins to be inserted into it easily. One
area of development that jumps to mind would be improving the security
features of BGP.