HTTP services
*************

Rotonda runs an HTTP server providing a (very basic) Web UI, metrics in
Prometheus format, and various JSON endpoints. All these are served on one
single port, configured in `rotonda.conf`.
Note that even though the endpoints are under ``/api/v1``, this does not
mean everything on this page is considered stable at this point.

Web UI
******

The web UI lives at the root of the configured web server. It provides a simple
overview of the basics. These pages should not be scraped, use the JSON
endpoints to fetch information properly.


Prometheus metrics
******************

On ``/metrics`` a Prometheus style file is served. This currently contains a
mix of metrics from Rotonda itself, and possibly user-defined metrics from
Roto filters. 

.. warning::

   The metrics defined by Rotonda itself are soon to be overhauled, and
   currently in sub-optimal shape after various refactors of the codebase. Some
   counters will always be 0, some will be incorrect. Use these to get a
   general idea of activity of the system, but not for accurate numbers
   whatsoever.


JSON endpoints
**************

.. important::

   While under ``/api/v1``, these endpoints are considered under development and
   might change without a version bump in the URL.

Rotonda offers endpoints to query information on `ingresses`, i.e. sources of
routing information such as BMP streams or BGP sessions, and on routes stored
in the RIBs. Both these endpoints allow filtering in the query part of the
request.


.. confval:: GET /api/v1/ingresses[?filter[A]=x[&filter[B]=y]..]

    Returns all the `ingresses` for this Rotonda instance. The filter options
    below can be combined, and will be evaluated in boolean **AND** fashion.

    - ``?filter[type]=<INGRESS_TYPE>``
        where **<INGRESS_TYPE>** can be one of
        ``bmp``,
        ``bgpViaBmp``,
        ``bgp``,
        ``mrt``.


    - ``?filter[ribType]=<RIB_TYPE>``
        where  **<RIB_TYPE>** can be one of 
        ``inPre``,
        ``inPost``,
        ``loc``,
        ``outPre``,
        ``outPost``.


    - ``?filter[peerAddress]=<IP_ADDR>``
        where **<IP_ADDR>** is an IPv6 or IPv4 address.


    - ``?filter[peerAsn]=<ASN>``
        where **<ASN>** is an Autonomous System Number, possibly prefixed with "AS".


.. confval:: GET /api/v1/ribs/ipv4unicast/routes/<IP_ADDR_PART>/<PREFIX_LENGTH>[?filter[A]=x[&filter[B]=y]..]

    Returns all the active routes for this IPv4 Unicast prefix. The filter
    options below can be combined, and will be evaluated in boolean **AND**
    fashion.

    Filters
    =======

    - ``?filter[originAsn]=<ASN>``
        where **<ASN>** is an Autonomous System Number, possibly prefixed with "AS".

    - ``?filter[otc]=<OTC>``
        filters on the Only-To-Customer path attribute,
        where **<OTC>** is an Autonomous System Number, possibly prefixed with "AS".

    - ``?filter[community]=<COMMUNITY>``
        filters on a standard Community (RFC1997),
        where **<COMMUNITY>** is either in canonical ``AS65412:666`` form, or 
        the name of a well-known communitiy e.g. ``NO_PEER``.

    - ``?filter[largeCommunity]=<LARGE_COMMUNITY>``
        filters on a Large Community (RFC8092),
        where **<LARGE_COMMUNITY>** is in canonical ``AS65412:1234:9999`` form.

    - ``?filter[ribType]=<RIB_TYPE>``
        where  **<RIB_TYPE>** can be one of 
        ``inPre``,
        ``inPost``,
        ``loc``,
        ``outPre``,
        ``outPost``.

    - ``?filter[rovStatus]=<ROV_STATUS>``
        where **<ROV_STATUS>** can be one of
        ``notChecked``,
        ``notFound``,
        ``valid``,
        ``invalid``.


    - ``?filter[peerAsn]=<ASN>``
        where **<ASN>** is an Autonomous System Number, possibly prefixed with "AS".

    Functions
    =========

    - ``?function[roto]=<ROTO_FUNCTION>``
        where **<ROTO_FUNCTION>** is the name of a user-defined Roto function
        taking path attributes as a parameter, and indicating via ``accept`` or
        ``reject`` whether a route should be included in the response.

        For example, the filter returns routes that contain both an ``OTC`` and
        ``AS_PATH`` path attribute where the ASN for the OTC is not part of the
        ``AS_PATH``.

        .. code-block:: rust

            fn my_filter_function(attr: Attributes) {
                match attr.otc() {
                    Some(otc) -> {
                        match attr.aspath() {
                            Some(aspath) -> {
                                if not aspath.contains(otc) {
                                    accept
                                } else {
                                    reject
                                }
                            },
                            None -> reject,
                        }
                    }
                    None -> { reject }
                }
            }


    Fields
    ======

    Fields can be used to override the default output fields of parts of the
    response. This can help to greatly reduce the size of responses. Note
    that this is different from *filtering*.

    - ``?fields[pathAttributes]=<LIST_OF_TYPECODES>``
        where **<LIST_OF_TYPECODES>** is a comma separated list of integers,
        representing one or multiple types of path attibutes. Only path
        attributes of these types will be included in the response.

      For example, to only return the Standard and Large communities:

      .. code-block::

        /api/v1/ribs/ipv4unicast/routes?fields[pathAttributes]=8,32
        

    Includes
    ========

    Includes are used to incorporate data additional to the exact prefix
    searched for. The ``filter``s and ``field``s are applied on these as
    well.

    .. danger::
        Including routes for more-specific prefixes via
        ``include=moreSpecifics`` can result in very large responses.
    
    - ``?include=<LIST_OF_INCLUDES>``
        where **<LIST_OF_INCLUDES>** is a comma separated list of one or
        multiple of:
        ``moreSpecifics``,
        ``lessSpecifics``.



    .. FIXME what about IngressId, why is this not in filter[] ?


.. confval:: GET /api/v1/ribs/ipv6unicast/routes/<IP_ADDR_PART>/<PREFIX_LENGTH>

    Returns all the active routes for this IPv6 Unicast prefix.

    Takes the same ``filter``, ``fields``, ``function`` and ``include`` as the
    ipv4 unicast endpoint described above.

.. danger::

    Depending on the volume of routes in the RIB, querying the endpoints below
    can be expensive, and/or result in huge responses.

.. confval:: GET /api/v1/ribs/ipv4unicast/routes


    Returns all the active routes for the entire IPv4 Unicast address family.

    This mimics a request to
    ``/api/v1/ribs/ipv4unicast/0.0.0.0/0?include=moreSpecifics`` and as such,
    all results will be part of the `included` object in the response:

    .. code-block::

        { ..
            "included": { "moreSpecifics": [ .. ] }
        }

    Takes the same ``filter``, ``fields``, ``function`` and ``include`` as the
    ipv4unicast endpoint described above.

   
.. confval:: GET /api/v1/ribs/ipv6unicast/routes

    Returns all the active routes for the entire IPv6 Unicast address family,
    similar to the IPv4 Unicast endpoint described above.


Deprecated endpoints
====================

The HTTP API offers endpoints for interacting with and monitoring Rotonda at
runtime:

.. confval:: GET /status                

    Human readable application status information.

.. confval:: GET /bmp-routers/

    Base path. Use the ``http_api_path`` configuration setting for the corresponding ``bmp-tcp-in`` component to change this URL.

.. confval:: GET /bmp-routers/<ROUTER_ID>

    This endpoint outputs information about the specified router if it is
    currently connected to the unit.

    A HTML table showing all currently monitored routers and some basic
    information about them.

    Three different forms of router ID are supported:

    - ``[SOURCE_IP]:[SOURCE_PORT]``, OR
    - ``[sysName]``, OR
    - ``[populated router_id_template]``

    Parameters:

    ``<ROUTER_ID>``          The id of the router to query information about.

.. confval:: GET /prefixes/<IP_ADDR_PART>/<PREFIX_LENGTH>[?includeMoreSpecifics|includeLessSpecifics]

    The RIB in the pipeline can be queried for prefixes with these URLs.

.. confval:: GET /mrt/<MRT_UNIT_NAME>/queue?file=<FILENAME>

    When configured with an `update_path`, a `mrt-file-in` can be instructed to
    add a file to its processing queue.

    Parameters:

    ``<FILENAME>``
    The path to an .mrt (or .gz, .bz2) file to be queued, relative to the
    configured `update_path`. The path may contain (relative) subdirectories,
    but the resulting file must reside under the configured `update_path`.
    For example, configured with ``update_path=my_mrt_files``, ``/queue?file=2025/01/30/updates1.mrt``


