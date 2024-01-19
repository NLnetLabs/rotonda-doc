Using Filters
=============

.. note::

   Make sure your Rotonda instance found and loaded the filter scripts upon
   startup before working your way through this section.

   If not, refer to :ref:`troubleshooting` or :doc:`/config/introduction`.


The filter scripts Rotonda uses are located in ``/etc/rotonda/filters`` if you
installed via a package directory. If you list the contents of that directory,
you'll notice a bunch of files of type ``.roto``, these are the files
containing the filters. Open the file called ``rib-in-pre-filter.roto`` with
your favourite text editor. It should look like this:

.. code:: text

  filter rib-in-pre-filter {
      define {
        rx msg: Route;
      }

      apply {
        accept;
      }
  }

This is the filter that gets run on any route that flows into the
``rib-in-pre`` RIB in Rotonda, this filter decides whether to store the route,
and subsequently pass it on to ``rib-in-post``.

Let's change this filter a bit, so that it look likes this:

.. code:: text

	filter rib-in-pre-filter {
	  define {
	    rx route: Route;
	  }

	  term my-asn {
	    match  {
	      route.as-path.origin() == AS64512;
	    }
	  }

	  apply {
	    filter match my-asn matching {
	      return reject;
	    };
	    accept;
	  }
	}

When your code looks good you can save it, and exit your text editor. So what
did we just do? Well, as we saw earlier Rotonda configured a few RIBs for you
out of the box. Each of these RIBs has a filter built in into it, in front of
the storage mechanism of the RIB. So the payload comes into the filter, the
filter creates a filtering decision based on the content of the payload and if
that decision is a resounding ``Accept``, it gets stored in the RIB. Each filter
consists of a script in a language we dubbed `Roto`, so each filter inside a
RIB is programmable. And so, we just re-programmed the filter inside the RIB
called ``rib-in-pre``.

Explaining our Filter
---------------------

So what does this script do? First of all, in the ``define`` section, we
defined the incoming *type* of our payload. For filters to be able to
meaningfully create a filtering decision it needs to know how the contents of
the payload can be parsed and this is exactly what specifying the type does.
`Roto` has built-in types: Primitive ones, like various integer types, a
string type and so on, and more complex ones especially for BGP/BMP
purposes, like ``BgpMessage`` and ``Route``. Finally, roto users can create their
own types, based on a `Record` or a `List`. In our `define` section the
keyword ``rx`` stands for the incoming payload ("receive"). We assign it to a
variable called ``route``, of type ``Route``. ``Route`` is a
built-in Roto type, that resembles a Record. This is the roto type that
Rotonda extracts from a BGP UPDATE message (or a BGP UPDATE message carried in a
BMP RouteMonitoring message), and is modeled after the way :RFC:`4271` uses the
term. It contains a prefix, the path attributes and some meta-data that were
found in a BGP UPDATE message. So a single BGP UPDATE may get transformed
into multiple routes, since a BGP UPDATE message can contain more than one
prefix in its NLRI. You can read more about the roto ``Route`` type
:doc:`here </roto/types>`. Suffices to say for now, that we can use the
payload-as-a-route to make filtering decisions with, and that's exactly what
we do in the rest of our roto script.

We have one ``term`` section in our script called `my-asn`. It contains one
match rule, that features our ``route`` variable, that has as its value our
incoming payload. With the expression ``route.as-path.origin() == AS64512`` we
create a comparison with the value returned from a method that is being called
on a field of the `route` variable. So this expression says: `if the origin of
the AS PATH atttribute of the incoming payload equals AS64512 then return
true``.

In the `apply` section - a roto script can only have one ``apply`` section -
`term` sections are bound to a filtering decision by means of one or more
`filter` expressions. In our script we only have one ``filter`` expression. It
states that the mentioned ``term`` should `match`, meaning it should return
``true``. Then, inside that ``filter`` block, the `return reject;` statement is
an early return from the whole script. The `accept` statement in the last line
of the `apply` section is the fall-through return value from the script if
nothing above it in the section matched. So our ``filter`` expression says:
"if the ``my-asn`` term returns ``true``, then return ``reject`` from our script. In
all other cases return ``accept``".

So, now we can assess the overall effect of our filter script, and that is:
`drop all routes that have AS64512 as the origin of the AS PATH`. In our
default BGP configuration AS64512 is defined as our ASN. In other words, this
filter script is an example of an iBGP filter.

Activating the modified Filter
------------------------------

We have changed the filter, we know what it is supposed to do now, but we
still have to activate the filter. We can do this by sending Rotonda the
``HUP`` signal. You can do this by issuing:

.. code:: shell-session

	$ killall -HUP rotonda

in a shell. In the log output you should see the confirmation of Rotonda
reloading the changed script:

.. code:: text

	[2023-12-11 13:34:42] INFO  SIGHUP signal received, re-loading roto scripts from location "/etc/rotonda/filters"
	[2023-12-11 13:34:42] INFO  Roto script /etc/rotonda/filters/bmp-in-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Re-loading modified Roto script /etc/rotonda/filters/rib-in-pre-filter.roto
	[2023-12-11 13:34:42] INFO  Roto script etc/rotonda/filters/rib-in-post-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Roto script etc/rotonda/filters/bgp-in-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Done reloading roto scripts

In the first line we see the confirmation that Rotonda received our signal,
and in the fourth line, we see confirmation that it is reloading our script.

.. Tip:: If you don't see any new logging information, then maybe your process is not precisely called rotonda. You can try `pgrep rotonda | xargs kill` and see if that works.

Trying the modified Filter
--------------------------

If you now restart the ``bmp-speaker`` tool that we used earlier, we can try
to send a few BMP messages and then see if our filter functions.

.. code:: console

	$ bmp-speaker --server localhost
	> initiation my-bmp-router "Mock BMP monitored router"
	> peer_up_notification global 0 10.0.0.1 65000 127.0.0.1 80 81 888 999 0 0
	> route_monitoring global 0 10.0.0.1 65000 0 none "e [65001,65002,64512] 10.0.0.1 NO_ADVERTISE 192.0.2.0/25"
	> route_monitoring global 0 10.0.0.1 65001 0 none "e [65001,65002,65003] 10.0.0.1 NO_EXPORT 192.0.2.128/25"

If you go to the HTTP/JSON interface of Rotonda then you can check that only
one route has been filtered out, and that one has passed through our filter
scripts and has been stored in the RIBs.

In the next chapter we will look at the configuration of the RIBs in Rotonda.
