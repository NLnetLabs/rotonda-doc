For this quick tour we assume that you have installed Rotonda via one of the
packages (see :doc:`Getting Started </installation>`), putting the required
configuration files in ``/etc/rotonda``.

If you built Rotonda from source, make sure you have the configuration files in
a similar directory structure. By default, Rotonda will look for the
**relative** ``etc/`` directory.


We’re only going to invoke the binary it installed directly in this quick
tour. Most probably you can just invoke the binary without further ado, as
``rotonda`` on the command line. If that does not work you might have to
restart your shell (to add the path to your default paths), or as a last
resort figure out the full path to the binary, and use that.

It probably helps if you’ve read the :doc:`Why does this exist? </about/why>`
section and/or :doc:`Overview </about/overview>` section, but you can also
learn on the job by following this tour, especially if you’re a bit familiar
with how a BGP speaker operates.

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

	Loading new Roto script etc/filters/bmp-in-filter.roto
	Loading new Roto script etc/filters/rib-in-pre-filter.roto
	Loading new Roto script etc/filters/rib-in-post-filter.roto
	Loading new Roto script etc/filters/bgp-in-filter.roto
	Listening for HTTP connections on 127.0.0.1:8080
	Starting target 'null'
	Starting unit 'rib-in-pre'
	Starting unit 'bmp-in'
	Starting unit 'bgp-in'
	Starting unit 'rib-in-post'
	All components are ready.
	All components are running.
	bmp-in: Listening for connections on 0.0.0.0:11019
	bgp-in: Listening for connections on 0.0.0.0:11179


.. note::

   If you see an error stating Rotonda failed to load Roto scripts however,
   please refer to `Unable to load Roto scripts`. You will not be able to
   complete the Quick Tour before fixing this.


Congratulations! You’ve successfully started the Rotonda daemon, but what did
you just do? Well, you’ve started the Rotonda daemon with a configuration that
we’ve created specially for the first, “minimal viable product” release. It
creates a pipeline that can ingress data from BMP and BGP sources, has two RIBs
and a few filters.

Before we go into details about that, let’s go over the output to STDOUT a
bit. The first few lines that mention :doc:`Roto </roto/introduction>` are
messages about filters that are being loaded in various places in the Rotonda
pipeline. The line following that is a HTTP web server that is started to host
requests from the users issued to any of the RIBs. Then there is a line about
a target ‘null’ being started, that’s the endpoint of the pipeline, in this
case it’s basically send to ``/dev/null``. 

Then a few lines about the units that are being started. Units are the parts
that together form the pipeline. They look innocuous.

Then following two lines for the ingress connector units, one for BGP
(``bgp-in``), and one for BMP ingress (``bmp-in``). Lastly, a confirmation
that everything’s ready and that everything’s successfully started.

We will learn more about all these components as we work our way through this
Quick Tour. First, we'll have a brief look at the HTTP, verifying it is working
as expected as we need it for the rest of this trip.

Using the HTTP service
----------------------

Rotonda is now waiting for input on one of its configured and running ingress
interfaces, not very exciting. We can however inspect some of its internal
state. If you let the shell with Rotonda running, open another shell and issue
this command:

.. code:: console

  $ curl http://localhost:8080/status


(Or open the URL in a browser; also make sure to **not** add a trailing slash)

Then you'll see a list of variables names with zeroes and minus ones as values.
Again, not super exciting, but at least we are seeing the confirmation that
it is running and waiting.

Now let’s query another endpoint, preferably in a browser (since it outputs
html): `<http://localhost:8080/bmp-routers/>`_.

Hopefully, you’ll see a (for now empty) table, with column headers hinting at
the type of information it will present once occupied.
So far, so good. Let’s fill this thing with some data.

.. 
