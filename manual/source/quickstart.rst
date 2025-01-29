For this quick start we assume that you already have installed Rotonda with
one of the methods described in the (see :doc:`Installation </installation>`)
section.

We will be invoking the Rotonda binary directly only, so either it needs to
live in your PATH environment variable, or you need to know the exact location
of the binary. If you used one of the packages you should be able to invoke
``rotonda`` in a shell directly. If you've installed with by using ``cargo``,
you may have to reload your shell before this works.

Configuration
-------------

Next up, we need an actual configuration file. If you've installed a package,
you will have a directory ``/etc/rotonda``, which will contain a file
``rotonda.conf``.

If you have built Rotonda with ``cargo install``, or from source, you should
create the directory ``/etc/rotonda`` yourself. You can copy the configuration
need for this quick start from the `Rotonda GitHub repository <https://
github.com/ NlnetLabs/rotonda/>`_.

Alternatively you can use this ``rotonda.conf``:

.. code-block:: toml

	http_listen = ["0.0.0.0:8080"]
	
	[units.bmp-in]
	type = "bmp-tcp-in"
	listen = "0.0.0.0:11019"
	http_api_path = "/bmp-routers/"

	[units.rib]
	type = "rib"
	http_api_path = "/rib/"
	sources = ["bmp-in"]

	[targets.null]
	type = "null-out"
	sources = ["rib"]

Starting a Rotonda instance
===========================

So, let’s invoke the binary directly. By default the binary will run as daemon
in the foreground, i.e. it will not exit unless you explicit kill by sending a
SIGINT signal, normally invoked by issuing a ``ctrl-c`` in the shell instance
that is running it. Let’s try:

.. code-block:: text

	$ rotonda -c /etc/rotonda/rotonda.conf

Hopefully you’ll see output like this:

.. code-block:: text

	Listening for HTTP connections on 0.0.0.0:8080
	Starting target 'null'
	Starting unit 'bmp-in'
	Starting unit 'rib'
	All components are ready.
	All components are running.
	bmp-in: Listening for connections on 0.0.0.0:11019

Congratulations! You've successfully started a Rotonda pipeline. Now, let's go over the output to see that we actually did.

The first line tells it that is has started a web server, listening on port
8080, and on all interfaces. The second three lines, starting with "Starting"
describe the components that are being started. In our case these are a Null
Target, a `bmp-tcp-in` unit called "bmp-in", and a RIB unit called "rib".
The next two lines, starting with "All components", tell us that the whole
pipeline is assembled, and was started correctly. Finally, the last line tells
that the `bmp-tcp-in` unit that we created is ready to receive BMP messages.

Using the HTTP service
----------------------

Rotonda is now waiting for input on one of its configured and running ingress
interfaces, not very exciting. We can however inspect some of its internal
state. If you let the shell with Rotonda running, open another shell and issue
this command:

.. code:: console

  $ curl http://localhost:8080/status


(Or open the URL in a browser; also make sure to **not** add a trailing slash)

Then you'll see a list of variables names with zeroes and minus ones as
values. Again, not super exciting, but at least we are seeing the confirmation
that it is running and waiting.

Now let’s query another endpoint, preferably in a browser (since it outputs
html): `<http://localhost:8080/bmp-routers/>`_.

Hopefully, you’ll see a (for now empty) table, with column headers hinting at
the type of information it will present once occupied.

Inserting data
--------------

To insert data into the Rotonda instance you have currently running you
will need a source of BMP messages, most likely a router that is able to
act as a "monitored router" (:RFC:`7854`), or a routing daemon that has that
capability. You'll have to configure that router or daemon to start a BMP
session with Rotonda to the correct IP address of the machine that rotonda
is running on (and reachable at), on port 11019. If for some reason you need
another port, you can change that port in the ``rotonda.conf`` file that is
currently used by Rotonda, and then send a SIGHUP to Rotonda. Restarting will
also work, of course.

If you don't have a router or routing daemon with BMP capabilities at your
disposal you can use the `mrt-file-in` connector. The next section describes this
process.

Using the `mrt-file-in` connector
---------------------------------

First, you'll have to download a ``mrt`` file from somewhere. Our suggestion is to download a bview file from the `RIS (Routing Information Service) <https://ris.ripe.net>`_ project, managed and hosted by the `RIPE NCC <https://www.ripe.net>`_. One of the smallest ``mrt`` files in the whole RIS project should be `this file <https://data.ris.ripe.net/rrc26/latest-bview.gz>`_. If you download this, or any other bview file from RIS, make sure to unpack ("gunzip") it.

The next step is to kill your Rotonda instance, and edit the configuration file to look like this:

.. code:: toml

	http_listen = ["127.0.0.1:8080"]

	[units.mrt-in]
	type = "mrt-file-in"
	# fill out the correct path to the downloaded bview file here.
	filename = "../bview/latest-bview-rrc26"

	[units.rib]
	type = "rib"
	sources = ["mrt-in"]

	[targets.null]
	type = "null-out"
	sources = "rib"

If you now restart Rotonda with the modified configuration, you should see
output like this:

.. code:: console

	Listening for HTTP connections on 127.0.0.1:8080
	Starting target 'null'
	Starting unit 'rib'
	Starting unit 'mrt-in'
	All components are ready.
	All components are running.
	processing ../bview/latest-bview-rrc26

A few seconds later (depending on your hardware) you should see this line added to your output:

.. code:: console

	mrt-in: done processing ../bview/latest-bview-rrc26, emitted 3501151 routes in 8s

Querying the RIB
----------------

.. tip::

	I really helps if you have ``curl`` and ``jq`` installed to query the JSON API.

You should now have routes loaded into the RIB in Rotonda, and we're now going
to query them. We have to do some second guessing as to what's in your RIB,
though. If you somehow loaded (at least) a full table, it shouldn't be too
hard. Let's try:

.. code:: console

	$ curl -s http://localhost:8080/prefixes/213.0.0.0/16 | jq .

You should see output that starts with a field called "data", filled with
a one or more objects, that all have distinct values in their "ingress_id"
field. Next to the "data" field, there should also be a field called
"included" that is has an empty object ("{]}") as value.

If you get an empty "data" field in the root, you could do one of two things.
First, query for a prefix that you know is actually in the data that you fed
into Rotonda, like so:

.. code:: console

	$ curl -s http://localhost:8080/prefixes/<ADDRESS_PART_OF_PREFIX>/<PREFIX_LENGTH> | jq .

Second, you could try to add another query parameter, called
``include=moreSpecifics``, like so:

.. code:: console

	$ curl -s http://localhost:8080/prefixes/<ADDRESS_PATH_OF_PREFIX>/<PREFIX_LENGTH>?include=moreSpecifics

If you try a fairly large prefix, say a /16, you increase the chance of
hitting an actual prefix.

Your output should now include all more specific prefixes found for the one
requested, in the "include" field in the root of the result JSON Object.

Adding a filter
---------------

Certain Rotonda components have filters built in. One of these components is a
RIB. The RIB filter can create a so-called verdict, ``accept`` or ``reject``,
that Rotonda uses to determine whether to store the route passing through the
filter in the RIB. The filter can also used to create a log message.

Let's create a filter. First, kill you current Rotonda instance. Second,
create a file called ``filters.roto``, preferably in the same directory as the
``rotonda.conf`` file you're using. It should contain this:

.. code:: roto

	filter rib-in-pre(
	    output: Log,
	    route: Route,
	    context: RouteContext,
	) {

	    define {
	        my_prefix = 209.127.80.0/20;
	    }

	    apply {
	        if route.prefix_matches(my_prefix) {
	            accept
	        } else {
	            reject            
	        }
	    }
	}


Now, add a line at the top of your ``rotonda.conf``:

.. code:: toml

	roto_script = "filters.roto"

Restart your Rotonda. If you now go to the status page, `<https://
localhost:8080/status>`_, you'll see that rib_unit_num_items is set to 1.
Rotonda filtered out all prefixes, except for the one we specified in the
``define`` section. If you now query this particular prefix in the RIB with:

.. code:: console

	curl -s http://localhost:8080/prefixes/209.127.80.0/20

You'll see approximately three entries in the "data" object: one for each peer
in the mrt file that announced this prefix to the RIS collector.
