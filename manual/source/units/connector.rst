Connector Units
================

Connectors are units that allow data to flow into a Rotonda application.
Currently Rotonda supports three different types of connectors. Connectors
can start and maintain sessions with other systems. Connectors therefore can
keep state.

bmp-tcp-in
==========

This unit implements an :RFC:`7854` "BGP Monitoring Protocol (BMP)" "monitoring
station" [1] by listening on a specified TCP/IP address and port number for
incoming connections from zero or more BMP capable routers. This unit
processes the incoming raw BMP messages through a BMP state machine in order
to extract, store and propagate downstream the route announcements and
withdrawals.

This unit extends the HTTP API with endpoints that output HTML and text
formatted information about the monitored routers currently streaming data
into Rotonda. These endpoints are intended for operators as a diagnostic aid
and not for automation purposes. The output format is not intended to be
machine readable and may change without warning.

Configuration Options
---------------------

.. confval:: type (mandatory)

This must be set to `bmp-tcp-in` for this type of connector.

.. confval:: listen (mandatory)

The IP address and the port to listen on for incoming BGP connections from BGP
speakers, in the form of: `"ip_address:port"`.
	
Example: ``listen = "0.0.0.0:11019"``.

.. confval:: http_api_path (optional)

The relative URL prefix for HTTP REST API calls responded to by this instance
of this unit.
	
Defaults to ``/routers/``.

bgp-tcp-in
==========

This unit listens on a specified TCP/IP address and port number for incoming
connections from zero or more :RFC:`4271` [1] BGP speakers. Currently supported
AFI/SAFI combinations are IPv4/Unicast, IPv6/Unicast, IPv4/Multicast and IPv6/
Multicast.

Configuration Options
----------------------

.. confval:: type (mandatory)

This must be set to `bgp-tcp-in` for this type of connector.

.. confval:: listen (mandatory)

The IP address and the port to listen on for incoming BGP connections from BGP
speakers, in the form of: `"ip_address:port"`.

Example: ``listen = "10.1.0.254:179"``

.. confval:: my_asn (mandatory)

The positive number of the Autonomous System in which this instance of Rotonda
is operating and which will be sent by this BGP speaker in its :RFC:`4271` BGP
OPEN message in the "My Autonomous Number" field [3]... confval:: my_bgp_id
(mandatory)

.. confval:: peers."address" (optional)

This setting define the set of peers from which (default: None) incoming
connections will be accepted. By default no such peers are defined and thus
all incoming connections are accepted. The double-quoted address value must
be an IPv4 or IPv6 address or a prefix (an IP address and positive integer
maximum length separated by a forward slash, e.g. "1.2.3.4/32"). The value of
this setting is a TOML table which may be specified inline or as a separate
section in the config file, e.g.:

.. code-block:: toml

	[units.my-bgp-in.peers.".."]
	name = ..
	remote_asn = ..


Or:

.. code-block:: toml

	[units.my-bgp-in]
	peers.".." = { name = .., remote_asn = .. }


.. confval:: protocols

The list of address families (AFI/SAFI) that is accepted from this peer. These
are announced in the BGP OPEN as MultiProtocol Capabilities (:RFC:`4760`).  In
order to receive 'as much as possible', list all options. If this setting is
omitted or set to the empty list, the session will only carry conventional
IPv4 Unicast information.

Currently supported are:
    ``Ipv4Unicast``, ``Ipv6Unicast``,
    ``Ipv4Multicast``, ``Ipv6Multicast``

mrt-in (experimental)
======================

This unit can take one or several ``mrt`` files (:RFC:`6396`) and emulate an
open BGP session with the contents of the table dumps in it.

It will all the RIB entries and load them into a Rotonda RIB. Routes will be
stored per peer.

.. confval:: type

This must be set to `mrt-in` for this type of connector.

.. confval:: filename

The path to the ``mrt`` file that will be loaded into the receiving RIB. Note
that this file should contain at least one table dump entry.
