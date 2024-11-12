Global Endpoints
================

The HTTP API offers endpoints for interacting with and monitoring Rotonda at
runtime:

.. confval:: GET /status                

    Human readable application status information

.. confval:: GET /routers/

    Base path. Use the <http_api_path> unit setting to change this if using
    multiple instances of this unit.

.. confval:: GET /routers/<ROUTER ID>

    This endpoint outputs information about the specified router if it is
    currently connected to the unit.

    A HTML table showing all currently monitored routers and some basic
    information about them.

    Three different forms of router ID are supported:

    - [SOURCE IP]:[SOURCE PORT], OR
    - [sysName], OR
    - [populated router_id_template]

    Parameters:

    <ROUTER ID>            The id of the router to query information about.


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
