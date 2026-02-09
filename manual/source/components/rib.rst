RIBs
====

This unit is a general purpose prefix store but is primarily intended to map
prefixes to the details of the routes to those prefixes and the source from
which they were received.

It offers a HTTP API for querying the set of known routes to a longest match
to a given IP prefix address and length.

The key of the RIB is the tuple ``(Prefix, ingress_id)``. This means that new
values for this key will override existing values in the RIB.

Upstream announcements cause routes to be added to the store. Upstream
withdrawals cause routes to be flagged as withdrawn in the store. Routes and
their withdrawals are stored per unique value of the field ``ingress_id`` in
the ``RouteContext`` object.

Pipeline Interaction
--------------------

The ``rib`` component ingests messages from type ``Route``, that maybe
accompanied by an object of type ``RouteContext``. It is first filtered,
and then may be stored in the RIB. Finally, it gets sent out if it was not
filtered out.

.. raw:: html

    <pre style="font-family: menlo,mono; font-weight: 400; font-size:0.75em;">
	                                        HTTP/API
	                                          │ ▲
	                                          │ │
	                               ┌──────────▼─┴─┐
	(Prefix,Route,RouteContext) ───▶ filter──▶RIB ├──▶ (Prefix,Route,RouteContext)
	                               └──────────────┘
	</pre>

Filtering
---------

The ``RIB`` component has a programmable Roto filter built-in with a
hard-coded name ``rib_in_pre``, and it should be included in the Roto filter
file specified in the Rotonda configuration. The type of this Roto filter is:

.. confval:: filter rib_in_pre(Log, Route, RouteContext) -> Verdict

	Argument Types
	--------------

	.. confval:: Log

	The output value that will be sent to a configured output, such as
	``mqtt-out``.

	.. confval:: Route (read-only)

	The Route that is flowing through this filter. It can be inspected,
	and will be sent out unmodified.

	.. confval:: RouteContext (read-only)

	Contextual data about the session.
	
	Return Value
	------------

	.. confval:: Verdict
	
	The resulting value of this filter, a of value ``accept`` or ``reject``.


Upon updates to the ROV status of a stored prefix, the function
``rib_in_rov_status_update`` is called. This happens when new RTR updates
(responses to Serial Queries, not the initial Cache Reset synchronisation) come
in. 

Note that this is a ``function``, not a ``filter``: there is no return type for
Rotonda to act upon afterwards.

.. _roto_rov_status_update:

.. confval:: function rib_in_rov_status_update(rov_update: RovStatusUpdate)

    .. confval:: rov_update

    Describes the previous and current :roto:ref:`RovStatus`
    (Valid/Invalid/NotFound) for a stored route. See :roto:ref:`RovStatusUpdate`
    for the available roto methods.

Configuration Options
---------------------

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

	Default: ``/prefixes/``

.. confval:: query_limits.more_specifics.shortest_prefix_ipv4 

	Default: ``8``

.. confval:: query_limits.more_specifics.shortest_prefix_ipv6 (def: 19)

	These two settings protect against overly broad queries that require more time
	to lookup longest matching prefixes in the store. Queries for IPv4 prefixes
	shorter than /8 (e.g. /7), or for IPv6 prefixes shorter than /19 (e.g. /18),
	will result in a HTTP 400 Bad Request status code.

	Default: ``8``
