HTTP API
========

The HTTP API offers endpoints for interacting with and monitoring Rotonda at
runtime:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Endpoint               Description
    ========================================================================
    /status                - Human readable application status information

    /[other]               - Some components (see below) offer their own HTTP
                             API endpoints.
    </pre>

.. [1]: https://prometheus.io/docs/introduction/overview/
.. [2]: https://prometheus.io/docs/visualization/grafana/

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    http_listen            The "<IP ADDRESS>:<PORT>" to listen on for 
                           incoming HTTP requests.
    </pre>


.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    The following OPTIONAL settings MAY be specified if desired:

    Setting                Description
    ========================================================================
    response_compression   Whether or not to GZIP compress responses if the
    (def: true)            client expresses support for it (via the HTTP
                            "Accept-Encoding: gzip" request header). Set to
                            false to completely disable GZIP response
                            compression.
    </pre>
