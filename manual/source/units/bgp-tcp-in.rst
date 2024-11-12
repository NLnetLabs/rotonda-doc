bgp-tcp-in
----------

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
	OPEN message in the "My Autonomous Number" field [3].

.. confval:: my_bgp_id (mandatory)

	An array of four positive integer numbers, e.g. [1, 2, 3, 4], which together define per RFC 4271 "A 4-octet unsigned integer that indicates the BGP Identifier of the sender of BGP messages" which is "determined up startup and is the same for every local interface and BGP peer" [2].

.. confval:: peers."<ADDRESS>" (optional)

	This setting defines the set of peers from which incoming connections will be accepted. By default no such peers are defined and thus all incoming connections are accepted.

	The double-quoted address value must be an IPv4 or IPv6 address or a prefix
	(an IP address and positive integer maximum length separated by a forward
	slash, e.g. "1.2.3.4/32").

	The value of this setting is a TOML table which may be specified inline or as
	a separate section in the config file, e.g.:

	.. code-block:: toml

		[units.my-bgp-in.peers.".."]
		name = ..
		remote_asn = ..

	Or:

	.. code-block:: toml

		[units.my-bgp-in]
		peers.".." = { name = .., remote_asn = .. }

	These sections have the following fields:

    .. confval:: name
	
	A name identifying the remote peer intended to make it easier for the operator to know which BGP speaker these settings refer to.

    .. confval:: remote_asn
	
	The positive number, or [set, of, numbers], of the Autonomous System(s) which from which a remote BGP speaker that connects to this unit may identify itself (in the "My Autonomous Number" field of the RFC 4271 BGP OPEN message [3]) as belonging to.

	Default: None

.. confval:: protocols

	The list of address families (AFI/SAFI) that is accepted from this peer. These
	are announced in the BGP OPEN as MultiProtocol Capabilities (:RFC:`4760`).  In
	order to receive 'as much as possible', list all options. If this setting is
	omitted or set to the empty list, the session will only carry conventional
	IPv4 Unicast information.

	Currently supported are: [``"Ipv4Unicast"``, ``"Ipv6Unicast"``, ``"Ipv4Multicast"``, ``"Ipv6Multicast"``]
