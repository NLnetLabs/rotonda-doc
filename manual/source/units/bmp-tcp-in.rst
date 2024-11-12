bmp-tcp-in
----------

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
