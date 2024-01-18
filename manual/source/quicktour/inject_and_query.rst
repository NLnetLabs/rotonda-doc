Injecting and querying for data
===============================

With the two ingress connectors up and running, our Rotonda instance is ready to
ingest information via BMP and BGP. We will focus on BMP, and for this tutorial,
we will be using artificial BMP data. If you have a (software) router capable of
producing a BMP stream and prefer to use that, study :doc:`Configuration
</config/introduction>` and continue with `Querying the RIBs`_ afterwards.

To inject the artificial BMP data, we are going to use our ``bmp-speaker`` tool.
In the next session, we will discuss how to install and use it.


Mocking Ingress Data
--------------------

The ``bmp-speaker`` tool can be installed with ``cargo``. We leave our Rotonda
running and open a new shell:

.. code:: console

	$ cargo install routes --bin bmp-speaker --version 0.1.0-rc0 --git https://github.com/NLnetLabs/routes


.. note ::

   If you do not have ``cargo`` available on your system, you probably want to
   check out the :ref:`Rust<rustup>` section on here to acquire a working
   toolchain with everything you need, without hassle.


This should make the ``bmp-speaker`` tool available. We can connect to our
Rotonda instance:

.. code:: console

	$ bmp-speaker --server localhost

You’ll be presented with a prompt, waiting for your input. We must mimic a real
BMP stream here, adhering to the BMP protocol standards, meaning that we:

    1. First send information about who (which router) is connecting (line 1 below),
    2. followed by information about one or more connected peers (line 2),
    3. followed by route information for those connected peers (line 3+4).

Copy these lines, in this order, into the prompt, and don't worry if not all of
these make sense (and yes, we are inserting /25's):

.. code:: shell-session

	$ bmp-speaker --server localhost
	> initiation my-bmp-router "Mock BMP monitored router"
	> peer_up_notification global 0 10.0.0.1 65000 127.0.0.1 80 81 888 999 0 0
	> route_monitoring global 0 10.0.0.1 65000 0 none "e [65001,65002,65003] 10.0.0.1 NO_ADVERTISE 192.0.2.0/25"
	> route_monitoring global 0 10.0.0.1 65001 0 none "e [65001,65002,65003] 10.0.0.1 NO_EXPORT 192.0.2.128/25"

If all’s well, you should not have gotten any errors, just a new prompt.
Let's verify Rotonda received the exported routing information by visiting
`<http://localhost:8080/bmp-routers/>`_ in a browser. (**Note:** the trailing
slash is required this time).

You should now see a table listing one monitored router, with the name and
description we used in the first input to ``bmp-speaker``.

Clicking on the `sysName` takes you to a details page for that connected router.
It includes a table describing all the connected Peers, showing the number of
prefixes obtained from each peer. Clicking on the number expands the table,
showing the prefixes we just fed into Rotonda via ``bmp-speaker``.

It also shows two links, ``rib-in-pre`` and ``rib-in-post``. These are the two
RIBs that Rotonda configured by default, referring to the contents of the
`Adj-RIB-In` (i.e., the received routes) for that peer before and after applying
any local policy, respectively. These links point to the RIB query endpoints and
should give back JSON instead of HTML. 

Looking at the URLs for those links gives an idea of how we can use these
endpoints: 'search RIB $R for prefix $P'. In the next section, we look at how we
can further refine such queries, and explain the output.


Querying the RIBs
-----------------

To reiterate: Rotonda creates an HTTP endpoint for every RIB, which means the
default configuration gives us http://localhost:8080/rib-in-pre and
https://localhost:8080/rib-in-post. Note that when requested like this, these
return an error. We need to create a proper query.

Before we dive into what these endpoints offer, make sure you are able to format
the returned JSON answers such that they are readable. If your browser does such
formatting (e.g. Firefox does), that's perfect. If you prefer to use the command
line with for example ``curl``, consider combining it with ``jq`` to format the
JSON output, as in our examples below.

.. note ::

    If you opted to you another source of data than the mock data using
    ``bmp-speaker`` as described in the previous step, the outputs in these
    examples will be different.


Now, let's start out with a simple query, one that might still be in your
browser form the previous steps after navigating through the HTML output:

.. code:: console

	$ curl -s http://localhost:8080/rib-in-post/192.0.2.0/25 | jq .

You should see output like this:

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
	

In the ``data`` object of this JSON output you see one of the routes that was
transmitted by our ``bmp-speaker`` to Rotonda. It contains the prefix, the BGP
path attributes, and some metadata such as the ``router_id`` field.


Let's query for a less-specific prefix that we did not explicitly fed into
Rotonda, specifying that we want to have more-specifics included in the response:

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

In this output, the ``data`` block is an empty array, because there were no
results found for the *exact* prefix we queried for. However, because we
specified the query parameter ``include=moreSpecifics`` in the URL, the
``included`` field hosts an object ``moreSpecifics`` with an array containing
the two routes we fed into Rotonda using ``bmp-speaker``.

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
the section on :doc:`RIB unit </units/rib>`.

Now that we know how to get data out of Rotonda, let's have a look at filters
and figure out how we can control what actually gets stored in the first place.


.. 
.. On Configuration
.. ================
.. 
.. We already talked a bit about how there are filters in our Rotonda setup, but
.. of course these are only going to be useful if you can change them. So let's
.. see how that works. We started Rotonda earlier without any configuration file
.. specified. This means that Rotonda used its internal configuration. Part of
.. this internal configuration is that it will look for a directory `etc/`,
.. relative to the current working directory. If that directory did not exist
.. Rotonda will disable all filters, meaning all incoming traffic will be
.. accepted. To be sure that we have filters installed, let's restart Rotonda.
.. Once we have filters installed we will be able to hot-reload them, meaning
.. that we can change them without restarting, thus not losing data in any of our
.. RIBs.
.. 
.. First, we are going to interrupt the current Rotonda, and after that we are
.. going to start a new Rotonda with a correct `etc/` path. Let's start.
.. 
.. Rotonda can be stopped by sending a SIGINT to the Rotonda process. This can be
.. done by pressing `ctrl-c` in the terminal where you started the Rotonda
.. process, or you can send a SIGINT signal to the process via either ``kill -INT
.. $(pidof rotonda)`` or ``killall -INT rotonda``.
.. 
.. Now we have to go to a working directory where we have a `etc/` directory. The
.. Rotonda source code repository contains this directory with `.roto` filter
.. files. It also has a ``rotonda.conf`` file. This configuration file contains the
.. same configuration as the built-in defaults in Rotonda.
.. 
.. So, if you have installed from source by using `cargo build` you can navigate
.. to the root of the ``rotonda`` repository by `cd`-ing into it and then just
.. start Rotonda from there.
.. 
.. If you have installed a package, e.g. a `.deb`, or `.rpm`, then a
.. `/etc/rotonda` directory was created. If you go to the root of your filesystem,
.. you can start Rotonda from there, and it will look for the directory
.. `/etc/rotonda/` and load all `.roto` files it can find in there.
.. 
.. After you have started Rotonda with one of these methods the first lines in
.. the log output should start with four `INFO` level lines, with a confirmation
.. for each roto filter file. If you see this `WARN` message:
.. 
.. .. code:: text
.. 
.. 	[2023-12-11 11:45:30] WARN  Roto filters 'bgp-in-filter','rib-in-pre-filter', 'bmp-in-filter', 'rib-in-post-filter' are referenced by your configuration but do not exist because no .roto scripts could be loaded from the configured `roto_scripts_path` directory 'etc/'. These filters will be ignored.
.. 
.. ... then our strategy failed, and we still don't have any filters. A method of
.. last resort would be to download the `/etc` directory from the source code
.. repository from `github.com
.. <https://github.com/NLnetLabs/rotonda/tree/main/etc>`_. Make sure you put the
.. files in a directory called `etc/` and copy all the files there. You can now
.. start Rotonda, by `cd`-ing into the parent of the `etc/` you created and then
.. start Rotonda with:
.. 
.. .. code:: console
.. 
.. 	rotonda -c etc/rotonda.conf
.. 
.. You should now see the four 'INFO' log lines with that confirm the loading of
.. the filter files.
.. 
.. You will also have to stop and restart the `bmp-speaker` tool. After you've
.. restarted that, do not replay the commands, but instead let's first edit a
.. filter.
