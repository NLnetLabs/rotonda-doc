Endpoints
================

The HTTP API offers endpoints for interacting with and monitoring Rotonda at
runtime:

.. confval:: GET /status                

    Human readable application status information

.. confval:: GET /bmp-routers/

    Base path. Use the ``http_api_path``` configuration setting for the corresponding ``bmp-tcp-in`` component to change this URL.

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

.. confval:: GET /<RIB_NAME>/prefixes/<IP_ADDR_PART>/<PREFIX_LENGTH>[?includeMoreSpecifics|includeLessSpecifics]

Pipeline Interaction

.. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                                HTTP API
                                    ^ |
                                    | |
                                    | v
                    +-------------------------------------+
        TCP/IP -->  | BmpMessage -> filter --> BmpMessage | --> N * Route
                    +----------------|--------------------+
                                     |
                                     v         
                        0..N output streams each
                        emitting values of a single RT
        </pre>

One Route value is output per prefix announced or withdrawn via a BGP UPDATE
message received as the payload of a BMP Route Monitoring message. Withdrawals
may also be synthesized due to BMP Peer Down notification or loss of TCP/IP
connection to the monitored BMP router.

.. [1]: https://www.rfc-editor.org/rfc/rfc7854
