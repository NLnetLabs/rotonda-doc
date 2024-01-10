For this quick tour we assume that you have installed Rotonda by using one of
the methods described in the :doc:`Getting Started </installation>` section.
We’re only going to invoke the binary it installed directly in this quick
tour. Most probably you can just invoke the binary without further ado, as
``rotonda`` on the command line. If that does not work you might have to
restart your shell (to add the path to your default paths), or as a last
resort figure the full path to the binary, and use that.

It probably helps if you’ve read the :doc:`Why does this exist? </about/why>`
section and/or :doc:`Overview </about/overview>` section, but you can also
learn on the job by following this tour, especially if you’re a bit familiar
with how a BGP speaker operates.

Run it
~~~~~~

So, let’s invoke the binary directly. By default the binary will run as daemon
in the foreground, i.e. it will not exit unless you explicit kill by sending a
KILLSIG signal, normally invoked by issuing a ``ctrl-C`` in the shell instance
that is running it. Let’s try:

.. code-block:: text

	$ rotonda

Hopefully you’ll see output like this:

.. code-block:: text

	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/filter.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/bmp-in-filter.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/rib-in-pre.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/bmp-in-post-filter.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/bgp-in-post-filter.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/rib-in-post.roto
	[2023-10-17 11:56:39] INFO  Loading new Roto script etc/bgp-in-filter.roto
	[2023-10-17 11:56:39] INFO  Listening for HTTP connections on 127.0.0.1:8080
	[2023-10-17 11:56:39] INFO  Starting target 'null'
	[2023-10-17 11:56:39] INFO  Starting unit 'bmp-tcp-in'
	[2023-10-17 11:56:39] INFO  Starting unit 'rib-in-post'
	[2023-10-17 11:56:39] INFO  Starting unit 'bmp-in'
	[2023-10-17 11:56:39] INFO  Starting unit 'bmp-in-filter'
	[2023-10-17 11:56:39] INFO  Starting unit 'bgp-in'
	[2023-10-17 11:56:39] INFO  Starting unit 'rib-in-pre'
	[2023-10-17 11:56:39] INFO  All components are ready.
	[2023-10-17 11:56:39] INFO  All components are running.
	[2023-10-17 11:56:39] INFO  bgp-in: Listening for connections on 0.0.0.0:11179
	[2023-10-17 11:56:39] INFO  bmp-tcp-in: Listening for connections on 0.0.0.0:11019

The first few lines of logging may also read something like

.. code-block:: text

  [2023-12-11 09:30:53] WARN  Unable to load Roto scripts: read directory error for path /Users/jasper/Projects/rotonda/rotonda-base/target/release/etc/: No such file or directory (os error 2).
  [2023-12-11 09:30:53] WARN  Roto filters 'rib-in-post-filter', 'bmp-in-filter', 'bgp-in-filter', 'rib-in-pre-filter' are referenced by your configuration but do not exist because no .roto scripts could be loaded from the configured `roto_scripts_path` directory 'etc/'. These filters will be ignored.

This sounds scary, but you can ignore it for now, we'll come back to it later.

Congratulations! You’ve successfully started the Rotonda daemon, but what did
you just do? Well, you’ve started the Rotonda daemon with a default
configuration that we’ve created specially for the first, “minimal viable
product” release. It creates a pipeline that can ingress data from BMP and BGP
sources, has two RIBs and a few filters.

Before we go into details about that, let’s go over the output to STDOUT a
bit. The first few lines that mention :doc:`Roto </roto/introduction>` are
messages about filters that are being loaded in various places in the Rotonda
pipeline. The line following that is a HTTP web server that is started to host
requests from the users issued to any of the RIBs. Then there is a line about
a target ‘null’ being started, that’s the endpoint of the pipeline, in this
case it’s basically send to ``/dev/null``. 

Then a few lines about the units that are being started. Units are the parts
that together form the pipeline. They look innocuous 

Then followed by two lines, one for each ingress connector unit, one for BGP
(``bgp-in``), and one for BMP ingress (``bmp-tcp-in``). Lastly, a confirmation
that everything’s ready and that everything’s successfully started.

TODO TODO lines about components. Should we have components mentioned here?
implementation details, I guess. TODO TODO reconcile ``bmp-tcp-in`` and
``bgp-in``

Querying the Instance
~~~~~~~~~~~~~~~~~~~~~

Rotonda is now waiting for input on one of its configured and running ingress
interfaces, not very exciting. We can however inspect some of its internal
state. If you let the shell with Rotonda running, open another shell and issue
this command:

.. code:: console

  $ curl http://localhost:8080/status


(Or open the URL in a browser; also make sure to **not** add a trailing slash)

Then you'll see a list of variables names with zeroes and minus ones as values.
Again, not super exciting, butß at least we are seeing the confirmation that
it is running and waiting.

Now let’s query another endpoint, preferably in a browser (since it outputs
html): `<http://localhost:8080/bmp-routers/>`_.

Hopefully, you’ll see something like this, but formatted differently, an empty
table:

.. code:: text

	Showing 1 monitored routers:    
	Router Address
		sysName
		sysDesc
		State
		# Peers Up/EoR Capable/Dumping
		# Invalid Messages (Soft/Hard Parse Errors)
	
	127.0.0.1:60205
		my-bmp-router
		Mock BMP monitored router
		Dumping
		1/1 (100%)/0 (0%)
		0 (1/0)

So far, so good. Let’s fill this thing with some data.

Mocking some Ingress Data
~~~~~~~~~~~~~~~~~~~~~~~~~

We have two ingress connectors up and running, a BGP and a BMP one, so you
could setup a BGP session with a routing daemon that speaks BGP, like `BIRD
<https://bird.network.cz/>`_ or `FRR <https://frrouting.org/>`_, or even a
session with a hardware BGP router. Likewise, you could set up a BMP session
with one of these (although BMP support is limited at this point in time,
still). If this is what you want you should read the :doc:`Configuration
</config/introduction>` chapter of this manual and you should be able to set
that up. 

To make things more snappy for our quick tour, we are going to use a tool that
we have created, called ``bmp-speaker``. It can be installed with ``cargo``,
the same tool that installed Rotonda for you:

.. code:: console

	$ cargo install routes --bin bmp-speaker --version 0.1.0-dev --git https://github.com/NLnetLabs/routes

When you’ve successfully installed it, we can try inserting routes into it.
Now, start a new shell and start the ``bmp-speaker`` tool. It will present you
a command line:

.. code:: console

	$ bmp-speaker --server localhost

You’ll be presented with a prompt, waiting for your input. Now, let’s input some of those:

.. code:: shell-session

	$ bmp-speaker --server localhost
	> initiation my-bmp-router "Mock BMP monitored router"
	> peer_up_notification global 0 10.0.0.1 65000 127.0.0.1 80 81 888 999 0 0
	> route_monitoring global 0 10.0.0.1 65000 0 none "e [65001,65002,65003] 10.0.0.1 NO_ADVERTISE 192.0.2.0/25"
	> route_monitoring global 0 10.0.0.1 65001 0 none "e [65001,65002,65003] 10.0.0.1 NO_EXPORT 192.0.2.128/25"

If all’s well, you should not have gotten any errors, just a new prompt. We
now have two processes running in two shells, one runs Rotonda, and one runs
``bmp-speaker``. The latter produced two routes and send those in a BMP
session to Rotonda. Let’s see if we can find that in Rotonda. 

In a browser you can now navigate to `<http://localhost:8080/bmp-routers/>`_,
and now you’ll see one entry in the table:

.. raw:: html

	<pre style="width:800px;font-size:0.8em;">Showing 1 monitored routers:
	<table width="600px">
	    <tbody>
	    <tr style="text-align:left">
	        <th>Router Address</th>
	        <th>sysName</th>
	        <th>sysDesc</th>
	    </tr>
			<tr>
				<td>127.0.0.1:61616</td>
				<td>my-bmp-router</td>
				<td>Mock BMP monitored router</td>
			</tr>
		  </tbody>
  	</table>
	</pre>

.. raw:: html

	<pre>
	<table>
	  <thead>
	    <tr>
	      <th colspan="2">The table header</th>
	    </tr>
	  </thead>
	  <tbody>
	    <tr>
	      <td>The table body</td>
	      <td>with two columns</td>
	    </tr>
	  </tbody>
	</table>
	</pre>
	
Your table should have more columns with more information. Also, the name of
the router you're connected to ("sysName"), should be a link. If you click
that you will be taken to new page that has more details about the connected
router. If you click once more on the link in the "Peers" table, all the way
down, the number "2" in the first row in the "#Prefixes" column, it will
expand into this:

.. raw:: html

	<pre style="font-size:0.8em;width:600px;">
	Announced prefixes:
		        192.0.2.128/25: <a href="/rib-in-post/192.0.2.128/25">rib-in-post</a> <a href="/rib-in-pre/192.0.2.128/25">rib-in-pre</a> 
		        192.0.2.0/25: <a href="/rib-in-post/192.0.2.0/25">rib-in-post</a> <a href="/rib-in-pre/192.0.2.0/25">rib-in-pre</a>
	</pre>

The links called ``rib-in-pre`` and ``rib-in-post`` are the two RIBs that
Rotonda configured by default. If you click one of them, you will taken to yet
again a new page filled with JSON, and the URL will have the name of the RIB
and the prefix in it. You've now hit one of the RIB query endpoints in
Rotonda.

Querying the RIBs
~~~~~~~~~~~~~~~~~

Rotonda creates a special HTTP endpoint that outputs JSON for every RIB that
it has created. By default, the HTTP server is running on ``localhost:8080``,
and the RIB endpoints live directly in the root of the URL path under their
name. As said, by default Rotonda creates two RIBS, so there is one endpoint
`<http://localhost:8080/rib-in-pre>`_ and one endpoint
`<https://localhost:8080/rib-in-post>`_. When requested like this they will
return nothing but an error. You should create a query, by issuing a prefix
that you want to query for, and, optionally you can include less and/or more
specific prefixes.

Since these are JSON endpoints, let's use ``curl`` to query them, if you have
``jq`` installed, you can pipe the output of curl into it. Do not worry if you
don't have ``jq``, just leave out the ``| jq .`` part. ``jq`` is only used
here to format the JSON output, there's no filtering or transformation going
on.

.. code:: console

	$ curl -s http://localhost:8080/rib-in-post/192.0.2.0/25 | jq .

You should now see output like this:

.. code:: json
	
	{
	  "data": [
	    {
	      "route": {
	        "prefix": "192.0.2.0/25",
	        "as_path": [
	          "AS65001",
	          "AS65002",
	          "AS65003"
	        ],
	        "origin_type": "Egp",
	        "next_hop": {
	          "Ipv4": "10.0.0.1"
	        },
	        "atomic_aggregate": false,
	        "communities": [
	          {
	            "rawFields": [
	              "0xFFFFFF02"
	            ],
	            "type": "standard",
	            "parsed": {
	              "value": {
	                "type": "well-known",
	                "attribute": "NO_ADVERTISE"
	              }
	            }
	          }
	        ],
	        "peer_ip": "10.0.0.1",
	        "peer_asn": 65000,
	        "router_id": "my-bmp-router"
	      },
	      "status": "InConvergence",
	      "route_id": [
	        0,
	        0
	      ]
	    }
	  ],
	  "included": {}
	}
	
In the ``data`` object of this JSON output you'll see one of the routes that
was transmitted by our ``bmp-speaker`` to Rotonda, with the BGP path
attributes that we're set, and some metadata, such as the ``router_id`` field.

Let's try another query:

.. code:: console

	$ curl -s http://localhost:8080/rib-in-post/192.0.2.0/24?include=moreSpecifics | jq .
	
.. code:: json

	{
	  "data": [],
	  "included": {
	    "moreSpecifics": [
	      {
	        "route": {
	          "prefix": "192.0.2.0/25",
	          "as_path": [
	            "AS65001",
	            "AS65002",
	            "AS65003"
	          ],
	          "origin_type": "Egp",
	          "next_hop": {
	            "Ipv4": "10.0.0.1"
	          },
	          "atomic_aggregate": false,
	          "communities": [
	            {
	              "rawFields": [
	                "0xFFFFFF02"
	              ],
	              "type": "standard",
	              "parsed": {
	                "value": {
	                  "type": "well-known",
	                  "attribute": "NO_ADVERTISE"
	                }
	              }
	            }
	          ],
	          "peer_ip": "10.0.0.1",
	          "peer_asn": 65000,
	          "router_id": "my-bmp-router"
	        },
	        "status": "InConvergence",
	        "route_id": [
	          0,
	          0
	        ]
	      },
	      {
	        "route": {
	          "prefix": "192.0.2.128/25",
	          "as_path": [
	            "AS65001",
	            "AS65002",
	            "AS65003"
	          ],
	          "origin_type": "Egp",
	          "next_hop": {
	            "Ipv4": "10.0.0.1"
	          },
	          "atomic_aggregate": false,
	          "communities": [
	            {
	              "rawFields": [
	                "0xFFFFFF01"
	              ],
	              "type": "standard",
	              "parsed": {
	                "value": {
	                  "type": "well-known",
	                  "attribute": "NO_EXPORT"
	                }
	              }
	            }
	          ],
	          "peer_ip": "10.0.0.1",
	          "peer_asn": 65000,
	          "router_id": "my-bmp-router"
	        },
	        "status": "InConvergence",
	        "route_id": [
	          0,
	          0
	        ]
	      }
	    ]
	  }
	}

Now in this output the ``data`` block is an empty array, meaning there were no
results found for the *exact* prefix you asked for. However, because we
specified the query parameter ``include=moreSpecifics`` in the URL, the
``included`` field hosts an object ``moreSpecifics`` with an array with two
routes: both the routes that the ``bmp-speaker`` fed into Rotonda.

And yes, you guessed it, there's also a query parameter argument
``lessSpecifics``, yielding similar results:

.. code:: console

	$ curl -s http://localhost:8080/rib-in-post/192.0.2.1/32?include=lessSpecifics | jq .

.. code:: json

	{
	  "data": [],
	  "included": {
	    "lessSpecifics": [
	      {
	        "route": {
	          "prefix": "192.0.2.0/25",
	          "as_path": [
	            "AS65001",
	            "AS65002",
	            "AS65003"
	          ],
	          "origin_type": "Egp",
	          "next_hop": {
	            "Ipv4": "10.0.0.1"
	          },
	          "atomic_aggregate": false,
	          "communities": [
	            {
	              "rawFields": [
	                "0xFFFFFF02"
	              ],
	              "type": "standard",
	              "parsed": {
	                "value": {
	                  "type": "well-known",
	                  "attribute": "NO_ADVERTISE"
	                }
	              }
	            }
	          ],
	          "peer_ip": "10.0.0.1",
	          "peer_asn": 65000,
	          "router_id": "my-bmp-router"
	        },
	        "status": "InConvergence",
	        "route_id": [
	          0,
	          0
	        ]
	      }
	    ]
	  }
	}
	
More details on the HTTP server and its endpoints for each RIB can be found in
the section about the :doc:`RIB unit </units/rib>`.

Using a Configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~

We already talked a bit about how there are filters in our Rotonda setup, but
of course these are only going to be useful if you can change them. So let's
see how that works. We started Rotonda earlier without any configuration file
specified. This means that Rotonda used its internal configuration. Part of
this internal configuration is that it will look for a directory `etc/`,
relative to the current working directory. If that directory did not exist
Rotonda will disable all filters, meaning all incoming traffic will be
accepted. To be sure that we have filters installed, let's restart Rotonda.
Once we have filters installed we will be able to hot-reload them, meaning
that we can change them without restarting, thus not losing data in any of our
RIBs.

First, we are going to interrupt the current Rotonda, and after that we are
going to start a new Rotonda with a correct `etc/` path. Let's start.

Rotonda can only be canceled by sending a SIGKILL to the rotonda process. This
can be done by pressing `ctr-c` in the terminal where you started the Rotonda
process, or you can send a SIGKILL signal to the process with the `kill` or
`killal` command.

Now we have to go to a working directory where we have a `etc/` directory. The
Rotonda source code repository contains this directory with `.roto` filter
files. It also has a `rotonda.conf` file. This configuration file contains the
same configuration as the default rotonda setup.

So, if you have installed from source by using `cargo build` you can navigate
to the root of the `rotonda` repository by `cd`ing into it and then just
restart `rotonda` from there.

If you have installed a package, e.g. a `.deb`, or `.rpm`, then a
`/etc/rotonda` directory was created. If you go to the root of your filesystem
than you can start Rotonda from there and then Rotonda will look for the
directory `/etc/rotonda/` and load all `.roto` files it can find in there.

After you have started rotonda with one of these methods the first lines in
the log output should start with four `INFO` level lines, with a confirmation
for each roto filter file. If you see this `WARN` message:

.. code:: text

	[2023-12-11 11:45:30] WARN  Roto filters 'bgp-in-filter','rib-in-pre-filter', 'bmp-in-filter', 'rib-in-post-filter' are referenced by your configuration but do not exist because no .roto scripts could be loaded from the configured `roto_scripts_path` directory 'etc/'. These filters will be ignored.

...then our strategy failed, and we still don't have any filters. A method of
last resort would be to download the `/etc` directory from the source code
repository from `github.com
<https://github.com/NLnetLabs/rotonda/tree/main/etc>`_. Make sure you put the
files in a directory called `etc/` and copy all the files there. You can now
start rotonda, by `cd`ing into the parent of the `etc/` you created and then
start rotonda with:

.. code:: console

	rotonda -c etc/rotonda.conf

You should now see the four 'INFO' log lines with that confirm the loading of
the filter files.

You will also have to stop and restart the `bmp-speaker` tool. After you've
restarted that, do not replay the commands, but instead let's first edit a
filter.

Modifying a Filter
~~~~~~~~~~~~~~~~~~

If you're not in the ``/etc`` directory, please `cd` into it. If you
look at the content of that directory, you'll notice a bunch of files of type
``.roto``, these are the files containing the filters. Open the file called
``rib-in-pre-filter.roto`` with your favourite text editor. It should look
like this:

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
~~~~~~~~~~~~~~~~~~~~~

So what does this script do? First of all, in the ``define`` section, we
defined the incoming *type* of our payload. For filters to be able to
meaningfully create a filtering decision it needs to know how the contents of
the payload can be parsed and this is exactly what specifying the type does.
`Roto` has built-in types, primitive ones, like various integer types, a
string type and so on, more complex built-in ones especially for BGP/BMP
purposes, like ``BgpMessage``, ``Route``. Finally, roto users can create their
own types, based on a `Record` or a `List`. In our `define` section the
keyword ``rx`` stands for the incoming payload ("receive"), we assign a
variable called ``route`` to it, and its type is ``Route``. ``Route`` is a
built-in Roto type, that resembles a Record. This is the roto type that
Rotonda extracts from a BGP message, and is modeled after the way :RFC:`4271`
uses the term. It contains a prefix, the path attributes and some meta-data
that were found in a BGP UPDATE message. So a BGP UPDATE may get transformed
into multiple routes, since a BGP UPDATE message can contain more than one
prefix in its NLRI(s). You can read more about the roto ``Route`` type
:doc:`here </roto/types>`. Suffices to say for now, that we can use the
payload-as-a-route to make filtering decisions with, and that's exactly what
we do in the rest of our roto script.

We have one ``term`` section in our script called `my-asn`, and it contains one
match rule, that features our ``route`` variable, that has as its value our
incoming payload. With the expression ``route.as-path.origin() == AS64512`` we
create a comparison with the value returned from a method that is being called
on a field of the `route` variable. So this expression says: `if the origin of
the AS PATH atttribute of the incoming payload equals AS64512 then return
true``.

In the `apply` section - a roto script can only have one ``apply`` section -
`term` sections are bound to a filtering decision by means of one or more
`filter` expressions. In our script we only have one ``filter`` expression. It
states that the mentioned ``term`` should return ``true``, by means of the `match`
statement. Then, inside that ``filter`` block The `return reject;` statement is
an early return from the whole script. The `accept` statement in the last line
of the `apply` section is the fall-through return value from the script if
nothing above it in the section is validated. So our ``filter`` expression says:
"if the ``my-asn`` term returns ``true``, then return ``reject`` from our script. In
all other cases return ``accept``".

So, now we can assess the overall effect of our filter script, and that is:
`drop all routes that have AS64512 as the origin of the AS PATH`. In our
default BGP configuration AS64512 is defined as our ASN. In other words, this
filter script is an example of an iBGP filter.

Activating the modified Filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have changed the filter, we know what it is supposed to do now, but we
still have to activate the filter. We can do this by sending Rotonda the
``HUP`` signal. You can do this by issuing:

.. code:: shell-session

	$ killall -HUP rotonda

in a shell. In the log output you should see the confirmation of rotonda
reloading the changed script:

.. code:: text

	[2023-12-11 13:34:42] INFO  SIGHUP signal received, re-loading roto scripts from location "etc/"
	[2023-12-11 13:34:42] INFO  Roto script etc/bmp-in-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Re-loading modified Roto script etc/rib-in-pre-filter.roto
	[2023-12-11 13:34:42] INFO  Roto script etc/rib-in-post-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Roto script etc/bgp-in-filter.roto is already loaded and unchanged. Skipping reload
	[2023-12-11 13:34:42] INFO  Done reloading roto scripts

In the first line we see the confirmation that Rotonda received our signal,
and in the fourth line, we see that confirmation that it is reloading our
script.

.. Tip:: If you don't see any new logging information, then maybe your process is not precisely called rotonda. You can try `pgrep rotonda | xargs kill` and see if that works.

Trying the modified Filter
~~~~~~~~~~~~~~~~~~~~~~~~~~

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
