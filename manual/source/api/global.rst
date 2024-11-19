Endpoints
================

The HTTP API offers endpoints for interacting with and monitoring Rotonda at
runtime:

.. confval:: GET /status                

    Human readable application status information in Prometheus format.

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

