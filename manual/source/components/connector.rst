Connectors
==========

Connectors are units that allow data to flow into a Rotonda application.
Currently Rotonda supports three different types of connectors. Connectors
can start and maintain sessions with other systems. Connectors therefore can
keep state.

bmp-tcp-in
----------

This unit implements an :RFC:`7854` "BGP Monitoring Protocol (BMP)"
"monitoring station" [1] by listening on a specified TCP/IP address and port
number for incoming connections from zero or more BMP capable routers. This
unit processes the incoming raw BMP messages through a BMP state machine in
order to extract, store and propagate downstream the route announcements and
withdrawals.

This unit extends the HTTP API with endpoints that output HTML and text
formatted information about the monitored routers currently streaming data
into Rotonda. These endpoints are intended for operators as a diagnostic
aid and not for automation purposes. The output format is not intended to be
machine readable and may change without warning.

Pipeline Interaction
--------------------

The ``bmp-tcp-in`` component ingests BMP Messages from a source over a
configured TCP session, optionally filters them, and explodes the NLRI
into separate ``(Prefix, Route, RouteContext)`` tuples, that are sent into the
pipeline.

Rotonda will assign one unique ``ingress_id`` per router present in the stream
produced by a ``bmp-tcp-in`` connector. Closing and opening the session may
lead to different ids per router.

.. raw:: html

	<pre style="font-family: menlo,mono; font-weight: 400; font-size:0.75em;">
	                       HTTP API
	                         │ ▲
	                         │ │
	          ┌──────────────▼─┴───────────────┐
	TCP/IP ───▶BmpMessage──▶filter──▶BmpMessage├──▶N * (Prefix,Route,RouteContext)
	          └───────────────┬────────────────┘
	                          │
	              ┌───────────▼──────────────┐
	              │0..M values of Log output │
	              └──────────────────────────┘
	</pre>

Filtering
---------

The ``bmp-tcp-in`` connector has a programmable Roto filter built-in with a
hard-coded name ``bmp-in``, and it should be included in the Roto filter file
specified in the Rotonda configuration. The type of this Roto filter is:

.. describe:: filter bmp-in(Log, BmpMsg, Provenance) -> Verdict

	Argument Types
	--------------

	.. describe:: Log

	Handle to emit log entries to a configured output, such as ``mqtt-out``.

	.. describe:: BmpMsg

	The BMP Message that is flowing through this filter. It can be inspected, 
	and will be sent out unmodified. Note that the individual parts of the
	NLRI of the message cannot be inspected. If you wish to do this, you
	should do this further in the pipeline, e.g. on the filter in a RIB.

	.. describe:: Provenance

	Contextual data about the session.
	
	Return Value
	------------

	.. describe:: Verdict
	
	The resulting value of this filter, either ``accept`` or ``reject``.

Configuration Options
---------------------

The ``bmp-tcp-in`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[units.<NAME>]
	type = "bmp-tcp-in"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.


.. describe:: type (mandatory)

This must be set to `bmp-tcp-in` for this type of connector.

.. describe:: listen (mandatory)

The IP address and the port to listen on for incoming BMP connections from
routers, in the form of: `"ip_address:port"`.
	
Example: ``listen = "0.0.0.0:11019"``.

.. describe:: http_api_path (optional)

The relative URL prefix for HTTP REST API calls responded to by this instance
of this unit.
	
Defaults to ``/bmp-routers/``.

bgp-tcp-in
----------

This unit listens on a specified TCP/IP address and port number for incoming
connections from zero or more :RFC:`4271` [1] BGP speakers. Currently
supported AFI/SAFI combinations are IPv4/Unicast, IPv6/Unicast, IPv4/Multicast
and IPv6/Multicast.

Pipeline Interaction
--------------------

The ``bgp-tcp-in`` component ingests BGP UPDATE Messages from a source,
optionally filters them, and explodes the NLRI into separate ``(Prefix, Route,
RouteContext)`` tuples, that are sent out into the pipeline.

Rotonda will create one unique ``ingress_id`` per session per ``bgp-tcp-in``
connector.

.. raw:: html

	<pre style="font-family: menlo,mono; font-weight: 400; font-size:0.75em;">
	          ┌──────────────────────────────────┐
	TCP/IP ───▶ BgpMessage──▶filter──▶BgpMessage ├──▶ N * (Prefix,Route,RouteContext)
	          └──────────────────────────────────┘
	</pre>

Filtering
---------

The ``bgp-tcp-in`` connector has a programmable Roto filter built-in with a
hard-coded name ``bgp-in``, and it should be included in the Roto filter file
specified in the Rotonda configuration. The type of this Roto filter is:

.. describe:: filter bgp-in(Log, BgpMsg, Provenance) -> Verdict

	Argument Types
	--------------

	.. describe:: Log

	Handle to emit log entries to a configured output, such as ``mqtt-out``.

	.. describe:: BgpMsg (read-only)

	The BGP UPDATE Message that is flowing through this filter. It can be
	inspected, and will be sent out unmodified.

	.. describe:: Provenance (read-only)

	Contextual data about the session.
	
	Return Value
	------------

	.. describe:: Verdict
	
	The resulting value of this filter, either ``accept`` or ``reject``.

Configuration Options
----------------------

The ``bgp-tcp-in`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[units.<NAME>]
	type = "bgp-tcp-in"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.

.. describe:: type (mandatory)

	This must be set to `bgp-tcp-in` for this type of connector.

.. describe:: listen (mandatory)

	The IP address and the port to listen on for incoming BGP connections from BGP
	speakers, in the form of: `"ip_address:port"`.

	Example: ``listen = "10.1.0.254:179"``

.. describe:: my_asn (mandatory)

	The positive number of the Autonomous System in which this instance of Rotonda
	is operating and which will be sent by this BGP speaker in its :RFC:`4271` BGP
	OPEN message in the "My Autonomous Number" field [3].

.. describe:: my_bgp_id (mandatory)

    An array of four positive integer numbers, e.g. [1, 2, 3, 4], which together
    define per RFC 4271 "A 4-octet unsigned integer that indicates the BGP
    Identifier of the sender of BGP messages" which is "determined up startup
    and is the same for every local interface and BGP peer" [2].

.. describe:: peers."<ADDRESS>" (optional)

    This setting defines the set of peers from which incoming connections will
    be accepted. By default no such peers are defined and thus all incoming
    connections are rejected.

    The double-quoted address value must be an IPv4 or IPv6 address or a prefix,
    e.g. "1.2.3.4" or "1.2.3.0/24.

    The value of this setting is a TOML table which may be specified inline or
    as a separate section in the config file, e.g.:

    .. code-block:: text

        [units.my-bgp-in.peers.".."]
        name = ..
        remote_asn = ..

    Or:

    .. code-block:: text

        [units.my-bgp-in]
        peers.".." = { name = .., remote_asn = .. }

    These sections have the following fields:

    .. describe:: name
	
    A name identifying the remote peer intended to make it easier for the
    operator to know which BGP speaker these settings refer to.

    .. describe:: remote_asn
	
    The expected Autonomous System Number for the remote BGP speaker that
    connects to this unit (i.e. the "My Autonomous Number"
    field of the RFC 4271 BGP OPEN message [3]).
    Can be specified as either a single ASN:

    .. code-block:: text

        remote_asn = 65001

    Or a list of multiple ASNs, where the empty list means 'accept everything':

    .. code-block:: text

        remote_asn = [] # accept any ASN sent by the peer
        remote_asn = [65001, 65002, 65003] # accept any of these ASNs

.. describe:: protocols

    The list of address families (AFI/SAFI) that is accepted from this peer.
    These are announced in the BGP OPEN as MultiProtocol Capabilities
    (:RFC:`4760`). In order to receive 'as much as possible', list all options.
    If this setting is omitted or set to the empty list, the session will only
    carry conventional IPv4 Unicast information.

    Currently supported are: [``"Ipv4Unicast"``, ``"Ipv6Unicast"``, ``"Ipv4Multicast"``, ``"Ipv6Multicast"``]

mrt-file-in `(experimental)`
----------------------------

This unit can take one or several ``mrt`` files (:RFC:`6396`) and ingest the
contents of the table dumps in it.

It will load all the RIB entries and load them into a Rotonda RIB. Routes will
be stored per peer.

Currently, the ``mrt-file-in`` connector does not offer any programmable
filtering.  You can, however, filter further on in the pipeline, e.g. in the
filter of a
receiving RIB.

Pipeline Interaction
--------------------

The ``mrt-file-in`` component ingests MRT messages from a file, extracts all the
peers mentioned in the ``PEER_INDEX_TABLE`` in the TableDump, and all the
BGP messages encapsulated in it. It then explodes all the BGP messages into
``(prefix, Route, RouteContext)`` tuples. It keeps a session open for the file
for the duration of the lifetime of the component.

Rotonda will assign one ``ingress_id`` per peer found in the TableDump table.

.. raw:: html

	<pre style="font-family: menlo,mono; font-weight: 400; font-size:0.75em;">
	        ┌──────────────────────────┐
	file ───▶ MrtMessage─┬▶BgpMessage  │
	        │            │             ├──▶ N * (Prefix,Route,RouteContext)
	        │            └▶RibTableDump│
	        └──────────────────────────┘
	</pre>


Configuration Options
---------------------

The ``mrt-file-in`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[units.<NAME>]
	type = "mrt-file-in"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.

.. describe:: type (mandatory)

	This must be set to `mrt-file-in` for this type of connector.

.. describe:: filename (mandatory)

	The path to the ``mrt`` file containing one or more table dump entries, that will be loaded into the receiving RIB.
