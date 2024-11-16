RIBs
====

This unit is a general purpose prefix store but is primarily intended to map
prefixes to the details of the routes to those prefixes and the source from
which they were received.

It offers a HTTP API for querying the set of known routes to a longest match
to a given IP prefix address and length.

Upstream announcements cause routes to be added to the store. Upstream
withdrawals cause routes to be flagged as withdrawn in the store.

Physical RIB
------------

The ``rib`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[units.<NAME>]
	type = "rib"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.

.. confval:: rib_type (mandatory)

	The type of this RIB. Can be either ``physical``, or ``virtual``.

.. confval:: sources (mandatory)

	An ["array", "of", "upstream", "unit", "names"] from which data will be received.

.. confval:: http_api_path

	The relative URL prefix for HTTP REST API calls responded to by this instance of this unit.

	Default: ``/<NAME>/prefixes/``

.. confval:: query_limits.more_specifics.shortest_prefix_ipv4 

	Default: ``8``

.. confval:: query_limits.more_specifics.shortest_prefix_ipv6 (def: 19)

	These two settings protect against overly broad queries that require more time
	to lookup longest matching prefixes in the store. Queries for IPv4 prefixes
	shorter than /8 (e.g. /7), or for IPv6 prefixes shorter than /19 (e.g. /18),
	will result in a HTTP 400 Bad Request status code.

	Default: ``8``
