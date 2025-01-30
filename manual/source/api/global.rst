Endpoints
================

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


