The Global Configuration File
=============================

.. warning::

    The current configuration setup of Rotonda has serious shortcomings. It
    will very likely change drastically in the near future.

This is the detailed description of what a global configuration file should
look like.

Global configuration happens in a file that by convention is called
``rotonda[.DESCRIPTION].conf``, e.g. a there is file called
``rotonda.example.conf``, that describes an example configuration.

This file must be in TOML format (https://toml.io/) and is structured as
follows:

- global settings
- 1 or more units
- 1 or more targets

Collectively units and targets are referred to as components.

Data flows from West to East beginning with at least one input unit, through
zero or more intermediate units and out terminating at at least one target.

Additionally Rotonda has HTTP interfaces to the North and output stream
interfaces to the South. The HTTP interfaces to the North may be used to
inspect and interact with the application. Some types of units and target
extend the HTTP interface with additional capabilities. The output stream
interfaces to the South provide support for alternate forms of output such as
MQTT event publication, logging/capture to file and proxying to external
parties.

Taken together one can think of the flow of information like so:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                                 (North)
                                HTTP APIs
                                   ^ |
                                   | |
                                   | v
       (West) BGP/BMP inputs --> pipeline --> BGP/BMP outputs (East)
                                    |
                                    |
                                    v
                              other outputs
                                 (South)
    </pre>

Data can only be successfully passed from one component to another if the
receiving component supports the value type output by the producing component.
Consult the "Pipeline interaction" sections in the documentation below to
ensure that your chosen inputs and outputs are compatible with each other.

A word about Components (Units & Targets)
--------------------------------------------

A unit is an input or intermediate processing stage. A target is a final
output stage. There must always be at least one unit with one downstream
target.

Unit and target definitions have similar forms:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    [units.[name]]                          [targets.[name]]
    type = "[type]"                         type = "[type]"
    ...                                     ...
    </pre>

Names must be unique, types must be valid and any mandatory settings specific
to the component type must be specified.

The currently available components are intended to be used like so:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
        bmp-tcp-in / bgp-tcp-in -> rib -> mqtt-out
    </pre>

Additionally there are some components intended for diagnostic use:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
        bmp-tcp-out, bmp-fs-out and null-out
    </pre>

Each unit is able to process certain types of input and emit certain types
of output. More information about each component type is given below.

A word about Roto Scripting
---------------------------

Some units and targets take one or more filter(-map) names which refer to
"filter" or "filter-map" blocks in any loaded Roto script files. Roto files
are written in the Rotonda Roto scripting language. Each file may contain a
mix of "filter" and "filter-map" blocks. "filter" blocks accept or reject
their Western input. "filter-map" blocks act the same but can also "map" the
input from the West to a different output on the East. Both "filter" and
"filter-map" blocks can also send data to one or more output streams to the
South.

Roto scripts work with Roto Types (RTs). All Roto script inputs, outputs and
intermediate values are Roto Types. Different units and targets accept and
produce different Roto Types and for a Rotonda pipeline to work properly input
and output types must be correctly aligned.

When Roto scripts send output to output streams to the South the data
published to the stream is in the form of a Roto Record type which consists of
key/value pairs, two of which have special meaning in Rotonda:

- name:  This key should have a string value which identifies the name of the
  target which is intended to handle the output Roto value. That target must
  still receive the value.
- topic: This key should have a string value which may be used by a target
  that processes the output Roto value to determine what to do with it, e.g.
  in the case of the MQTT target it can be used to influence the eponymous
  MQTT topic to which a message will be published.

The following OPTIONAL settings MAY be specified if desired:


.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    roto_scripts_path      A "path/to/a/directory/containing/*.roto" script
    (def: None)            files. Each script file will be loaded & compiled
                           and may be referred to in unit and target
                           settings by using the name of a filter defined in
                           the script file with the filter_name setting of
                           the unit or target.
    </pre>

Note: In the diagrams below the term "RT" denotes any valid Roto scripting
type.

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


Unit: bgp-tcp-in
================

This unit listens on a specified TCP/IP address and port number for incoming
connections from zero or more RFC 4271 [1] BGP speakers.

The following MANDATORY settings MUST be specified:


.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    listen                 The "<IP ADDRESS>:<PORT>" to listen on for
                            incoming BGP connections from BGP speakers.

    my_asn                 The positive number of the Autonomous System in
                            which this instance of Rotonda is operating and
                            which will be sent by this BGP speaker in its
                            RFC 4271 BGP OPEN message in the "My Autonomous
                            Number" field [3].

    my_bgp_id              An array of four positive integer numbers, e.g.
                            [1, 2, 3, 4], which together define per RFC 4271
                            "A 4-octet unsigned integer that indicates the
                            BGP Identifier of the sender of BGP messages"
                            which is "determined upon startup and is the same
                            for every local interface and BGP peer" [2].
    </pre>

The following OPTIONAL settings MAY be specified if desired:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                 Description
    ========================================================================
    peers."address"         This setting define the set of peers from which
    (def: None)             incoming connections will be accepted. By default
                            no such peers are defined and thus all incoming
                            connections are accepted.

                            The double-quoted address value must be an IPv4
                            or IPv6 address or a prefix (an IP address and
                            positive integer maximum length separated by a
                            forward slash, e.g. "1.2.3.4/32").

                            The value of this setting is a TOML table which
                            may be specified inline or as a separate section
                            in the config file, e.g.:

                                [units.my-bgp-in.peers.".."]
                                name = ..
                                remote_asn = ..

                            Or:

                                [units.my-bgp-in]
                                peers.".." = { name = .., remote_asn = .. }

    filter_name             The name of a loaded "filter" or "filter-map"
                            that will be executed for every BGP UPDATE PDU
                            received by this unit. If the script terminates
                            with "reject" the UPDATE PDU will be discarded
                            as if it had never been received.

    protocols               The list of address families (AFI/SAFI)
                            that is accepted from this peer. These are
                            announced in the BGP OPEN as MultiProtocol
                            Capabilities (RFC4760).  In order to receive 'as
                            much as possible', list all options.
                            If this setting is omitted or set to the empty
                            list, the session will only carry conventional IPv4
                            Unicast information.

                            Currently supported are:
                                Ipv4Unicast, Ipv6Unicast,
                                Ipv4Multicast, Ipv6Multicast,
                                Ipv4MplsUnicast, Ipv6MplsUnicast,
                                Ipv4MplsVpnUnicast, Ipv6MplsVpnUnicast,
                                Ipv4RouteTarget,
                                Ipv4FlowSpec, Ipv6FlowSpec,
                                L2VpnVpls, L2VpnEvpn

    addpath                 The list of address families (AFI/SAFI) for which
                            ADDPATH Capabilities (RFC7911) will be announced in
                            the BGP OPEN sent to this peer.  If this setting is
                            omitted or set to the empty list, no capabilities
                            is announced. Supported address families are the
                            same as listed for the 'protocols' setting above,
                            though they do not make sense in all cases.
    </pre>

The following MANDATORY settings MUST be specified in a peers."address"
table:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    name                   A name identifying the remote peer intended to
                            make it easier for the operator to know which
                            BGP speaker these settings refer to.

    remote_asn             The positive number, or [set, of, numbers], of
                            the Autonomous System(s) which from which a
                            remote BGP speaker that connects to this unit may
                            identify itself (in the "My Autonomous Number"
                            field of the RFC 4271 BGP OPEN message [3]) as
                            belonging to.
    </pre>           

Pipeline Interaction
    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">

                   +-------------------------------------------------+
        TCP/IP --> | BgpUpdateMessage -> filter --> BgpUpdateMessage | --> N * Route
                   +-----------------------|-------------------------+
                                           |
                                           v         
                                0..N output streams each
                                emitting values of a single RT
        </pre>

One Route value is output per prefix announced or withdrawn via a BGP UPDATE
message received. Withdrawals may also be synthesized if the BGP session is
disconnected or the TCP/IP connection to the remote BGP speaker is lost.

.. [1]: https://www.rfc-editor.org/rfc/rfc4271
.. [2]: https://www.rfc-editor.org/rfc/rfc4271#section-1.1
.. [3]: https://www.rfc-editor.org/rfc/rfc4271#section-4.2


Unit: bmp-tcp-in
================

This unit implement an RFC 7854 "BGP Monitoring Protocol (BMP)" "monitoring
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

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    listen                 The "[IP ADDRESS]:[PORT]" to listen on for
                            incoming BGP connections from BGP speakers.

    The following OPTIONAL settings MAY be specified if desired:

    Setting                Description
    ========================================================================
    http_api_path          The relative URL prefix for HTTP REST API calls
    (def: /routers/)       responded to by this instance of this unit.

    router_id_template     A user defined "[string]" that is used to name
    (def: {sys_name})      incoming router connections according to a user
                            supplied template which may include the following
                            placeholders which will be expanded into their
                            respective values for the monitored router.

                                {sys_name}    - Router RFC 7854 sysName.
                                {router_ip}   - Router source IP address.
                                {router_port} - Router source port.

                            Note: {sys_name} will be "unknown" until the
                            sysName information TLV is received from the
                            router as part of the BMP Initiation Message that
                            it is required to send before any other messages.

    filter_name            The name of a loaded "filter" or "filter-map"
                            that will be executed for every BMP message
                            received by this unit. If the script terminates
                            with "reject" the BMP message will be discarded.
                            as if it had never been received.

    tracing_mode           Whether and how to trace BMP messages through the
    (def: Off)             pipeline.

                            When set to "On" all received BMP messages will
                            be traced into successive tracing buffers
                            numbered 0-255 inclusive. These can be seen on
                            the status graph at:

                                /status/graph/traces/N.

                            When set to "IfRequested" received BMP messages
                            whose upper niblle of the "Version" header byte
                            is non-zero will cause that unsigned integer
                            number to be used as the tracing buffer index to
                            capture traces into.
    </pre>

HTTP API Endpoints
------------------

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    REQUESTS:

        GET /routers/
        GET /routers/[ROUTER ID]

    DESCRIPTION:

        This endpoint outputs information about the specified router if it is
        currently connected to the unit.
    </pre>

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    PARAMETERS:

    Parameter              Description
    ========================================================================
    /routers/              Base path. Use the <http_api_path> unit setting
                            to change this if using multiple instances of
                            this unit.

    <ROUTER ID>            The id of the router to query information about.
                            Three different forms of router ID are supported:

                            - [SOURCE IP]:[SOURCE PORT], OR
                            - [sysName], OR
                            - [populated router_id_template]

    RESPONSE: GET /routers/

        A HTML table showing all currently monitored routers and some basic
        information about them.

    RESPONSE: GET /routers/<ROUTER_ID>

        A detailed plain text report about the monitored router and its
        interactions with Rotonda.
    </pre>

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




Unit: filter
============

This unit runs a filter script that can be either a filter or a filter-map:

  - A filter accepts or rejects the input Roto value that it receives.
  - A filter-map does the same but the output Roto value can be different than
    the input value, i.e. as if the input was "mapped" to the output.
  - Both filter and filter-map scripts can optionally emit additional Roto
    values for consumption by particular targets.

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    sources                An ["array", "of", "upstream", "unit", "names"]
                            from which data will be received.

    filter_name            The name of a loaded "filter" or "filter-map"
                            that will be executed for every pipeline payload
                            received by this unit. If the script terminates
                            with "reject" the payload item will be discarded.
    </pre>

Pipeline Interaction
    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                                +--------+
                         RT --> | filter | --> Accept with RT, or Reject
                                +--------+
                                     |
                                     |
                                     v
                            0..N output streams each
                        emitting values of a single RT
        </pre>


Unit: rib
=========

This unit is a general purpose prefix store but is primarily intended to map
prefixes to the details of the routes to those prefixes and the source from
which they were received.

It offers a HTTP API for querying the set of known routes to a longest match
to a given IP prefix address and length.

Upstream announcements cause routes to be added to the store. Upstream
withdrawals cause routes to be flagged as withdrawn in the store.

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    sources                An ["array", "of", "upstream", "unit", "names"]
                            from which data will be received.

    The following OPTIONAL settings MAY be specified if desired:

    Setting                Description
    ========================================================================
    http_api_path          The relative URL prefix for HTTP REST API calls
    (def: /prefixes/)      responded to by this instance of this unit.

    query_limits.more_specifics.shortest_prefix_ipv4 (def: 8)
    query_limits.more_specifics.shortest_prefix_ipv6 (def: 19)
                            These two settings protect against overly broad
                            queries that require more time to lookup longest
                            matching prefixes in the store. Queries for IPv4
                            prefixes shorter than /8 (e.g. /7), or for IPv6
                            prefixes shorter than /19 (e.g. /18), will result
                            in a HTTP 400 Bad Request status code.

    rib_keys (def: ["PeerIp", "PeerAsn", "AsPath"])
                            Adjust this setting to control when routes are
                            considered to be from the same peer and thus when
                            that peer announces a route does it update or is
                            in addition to an existing announcement, or when
                            that peer withdraws a route, or its routes are
                            withdrawn because the connection to it is lost,
                            that only announced routes whose specified key
                            fields match those of the withdrawal will be
                            marked as withdrawn. Incorrectly specifying the
                            set of key fields can lead to a different set of
                            announced routes stored in the rib than expected.

    filter_name            Either a single name of a loaded "filter" or
                            "filter-map", or an ["array", "of", "filter",
                            "or", "filter-map", "names"]. If more than one is
                            specified, the additional entries cause virtual
                            RIB units to be created to the East of this unit,
                            each subsequent virtual RIB being further to the
                            East than the last. The input type received by
                            each "filter" or "filter-map" depends on the
                            output type of the previous RIB unit. Each vRIB
                            exposes its own HTTP REST API endpoint at
                            {http_api_path}/{n}/ where {n} is zero for the
                            first vRIB, 1 for the second vRIB, and so on.
    </pre>

Pipeline Interaction
    In summary the flow looks like this:

    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
        RT --> filter1 --> pRIB --> filter2 --> vRIB1 --> filter2 --> vRIB2 --> ..
        </pre>

    Now lets break down the various different possible scenarios into more
    detail:

    1. A single physical RIB with no Roto script filtering:

    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                                    HTTP API
                                       ^ |
                                       | |
                                       | v
                                    +------+
                             RT --> | pRIB | --> RT
                                    +------+
        </pre>



    2. A single physical RIB with a Roto script filter:

    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">

                                    HTTP API
                                        ^ |
                                        | |
                                        | v
                                     +------+
            RT --> filter --> RT --> | pRIB | --> RT
                     |               +------+
                     |
                     v         
            0..N output streams each   
            emitting values of a single RT
        </pre>


    3. A physical RIB and a virtual RIB, each with their own Roto script filter:

    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">

                                    HTTP API
                                       ^ |
                                       | |
                                       | v
                                    +------+
           RT --> filter --> RT --> | pRIB | --> RT -->+
                    |               +------+           |  
                    |                                  |
                    v                                  |
            0..N output streams each                   |
            emitting values of a single RT             |
                                                       v
            +<-----------------------------------------+
            |
            |                       HTTP API
            |                         ^ |
            |                         | |
            |                         | v
            v                      +------+
            +--> filter --> RT --> | vRIB | --> RT
                    |              +------+                    
                    |
                    v         
            0..N output streams each   
            emitting values of a single RT
        </pre>

.. tip:: 
 
    Queries to the HTTP API of a virtual RIB are submitted upstream to the
    physical RIB and the results flow back down the pipeline to the
    requesting virtual RIB and out via its HTTP API. Results are processed
    through each vRIB filter yielding the vRIB modified "view" of the result
    data.

.. tip:: Values emitted by output streams of vRIB filters when processing
    HTTP API query results are silently discarded, i.e. values emitted by
    output streams of vRIB filters are only honoured for input data that
    originated to the West of the pRIB, NOT for data that was the result
    of a HTTP API query.

.. tip:: The input to a physical RIB is usually a Route but can also be a Record
 with a "prefix" key, but only Route values support the notion of being
 "withdrawn". The entire record (all its keys and values) will be added
 to the set of values stored at the prefix in the RIB, with the rib_keys
 fields determining whether a new value is added to the set or replaces
 an existing item in the set.

Target: mqtt-out
================

This target publishes JSON events to an MQTT broker via a TCP connection.

.. tip:: The MQTT broker is not part of Rotonda, it is a separate service that
    must be deployed and operated separately to Rotonda.

Tested with the EMQX MQTT broker with both the free public MQTT 5 Broker [1]
and with the EMQX Docker image [2].

This target ONLY accepts input data that:

- Was received from a configured upstream source unit.
- Was emitted by a Roto script output stream.
- Is of type Record with a "name" field whose value matches the name of this
  instance of the mqtt-out target.

So naming an instance of this unit in a Roto script output stream record is
not sufficient to have this unit receive it, this unit must still be
downstream of the producing unit to receive its output.

The JSON event structure produced by this target is a direct serialization
of the received Roto type as JSON, i.e. a record with a set of key/value
pairs.

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    sources                An ["array", "of", "upstream", "unit", "names"]
                            from which data will be received.

    destination            A "host:port" string specifying the host or IP
                            address of an MQTT broker to connect to. If the
                            ":port" part is omitted the IANA registered MQTT
                            port number [3] 1883 will be used. Note: Only
                            unencrypted TCP connections are supported, i.e.
                            TLS and WS are not supported.

    The following OPTIONAL settings MAY be specified if desired:

    Setting                Description
    ========================================================================
    client_id              A unique name to identify the client to the
    (def: "")              server in order to hold state about the session.
                            If empty the server will use a clean session and
                            assign a random name to the client. Servers are
                            required to support names upto 23 bytes in length
                            but may support more.

    qos                    MQTT quality-of-service setting for determining
    (def: 2)               how many times a message can be delivered:

                                0 (at most once)
                                1 (at least once)
                                2 (exactly once)

                            Higher values require more synchronization with
                            the broker leading to lower throughput but
                            greater reliability/correctness.

    queue_size             The number of messages that can be buffered for
    (def: 1000)            delivery to the MQTT broker.

    connect_retry_secs     The number of seconds to wait before attempting
    (def: 60)              to reconnect to the MQTT broker if the connection
                            is lost.

    publish_max_secs       The number of seconds to wait before timing out
    (def: 5)               an attempt to publish a message to the MQTT
                            broker.

    topic_template         A "string" template that will be used to 
    (def: "rotonda/{id}")  determine the MQTT topic to which events will be
                            published. If present, the "{id}" placeholder
                            will be replaced by the "topic" value in the
                            incoming Record value. When using "{id}" an MQTT
                            client that supports MQTT wildcards can still 
                            receive all events by subscribing to 'rotonda/#'
                            for example.

    username               A "string" username for login to the MQTT broker.

    password               A "string" password for login to the MQTT broker.
    </pre>

Pipeline Interaction
    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                            +----------+
                 Record --> | mqtt-out | - - JSON - - > MQTT server
                            +----------+
        </pre>

.. [1]: https://www.emqx.com/en/mqtt/public-mqtt5-broker
.. [2]: https://hub.docker.com/r/emqx/emqx
.. [3]: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=mqtt

Target: null-out
================

This target discards everything it receives.

Rotonda requires that there always be at least one target. Using this target
allows you to run Rotonda for testing purposes without any "real" targets,
or if the only output is via Roto script output stream messages.

The following MANDATORY settings MUST be specified:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
    Setting                Description
    ========================================================================
    source                 The upstream unit from which data will be
                            received.
    </pre>

Pipeline Interaction
    .. raw:: html

        <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">

                                +----------+
                         RT --> | null-out |
                                +----------+
        </pre>

.. Target: bmp-fs-out
.. ------------------

.. .. WARNING

..     This section is part of the BMP proxy, that is currently disabled

.. This target writes raw BMP messages to files on disk, either separated per
.. monitored router or merged into a single file. BMP messages can be written
.. in one of three different formats:

..   log, raw, or pcap text

.. The log format is a limited one line per BMP message plain text log of BMP
.. messages received and some limited information about each one. This format
.. is intended for gaining a quick insight into the messages being received by
.. Rotonda.

.. The raw format writes the received BMP bytes out as-is, with each BMP
.. message byte sequence preceeded by a number indicating how many BMP message
.. bytes follow. This format is intended for capturing messages for replay for
.. testing purposes later.

.. THe PCAP text format can be transformed by the separate text2pcap tool, and
.. from there can be viewed and analyzed using a tool like WireShark.
 
.. --- Settings ---------------------------------------------------------------

.. The following MANDATORY settings MUST be specified:

.. Setting                Description
.. ========================================================================
.. source                 The upstream unit from which data will be
..                         received.

.. path                   The path to which files will be written. If mode
..                         is "split" (the default) this setting specifies
..                         a directory (which must already exist) under
..                         which one file per router will be created.

.. format                 Choose one of: "log", "raw", or "pcaptext".

.. The following OPTIONAL settings MAY be specified if desired:

.. Setting                Description
.. ========================================================================
.. mode                   Either "merge" or "split". In merged mode all BMP
.. (def: "split")         messages from all monitored routers are appended
..                         to the same file. In split mode separate output
..                         files will be written under an EXISTING directory
..                         specified by the "path" setting. In "merge" mode
..                         all BMP messages from all monitored routers will
..                         be written into a single file file defined by the
..                         "path" setting.

.. --- Pipeline interaction ---------------------------------------------------

.. .. raw:: html

..     <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">

..                               +------------+
..                BmpMessage --> | bmp-fs-out | - - - - > Writes to disk
..                               +------------+
..     </pre>

.. Target: bmp-tcp-out
.. -------------------

.. This target writes raw BMP messages over a TCP connection to a specified
.. destination IP address and port number, for instance to a second instance of
.. Rotonda.
 
.. --- Settings ---------------------------------------------------------------

.. The following MANDATORY settings MUST be specified:

.. Setting                Description
.. ========================================================================
.. sources                An ["array", "of", "upstream", "unit", "names"]
..                         from which data will be received.

.. destination            A TCP IP address and port number to proxy raw BMP
..                         messages to.

.. The following OPTIONAL settings MAY be specified if desired:

.. Setting                Description
.. ========================================================================
.. accept                 Zero or more "IP address" values defining routers
.. (def: [])              whose BMP messages will be proxied. If specified,
..                         ONLY the specified routers will be proxied, all
..                         others will be able to connect and send messages
..                         to Rotonda.

.. reject                 Zero or more "IP address" values defining routers
.. (def: [])              whose BMP messages will NOT be proxied. If
..                         specified and "accept" is NOT specified, this
..                         setting will permit all other monitored routers
..                         BMP messages to be proxied.

.. --- Pipeline interaction ---------------------------------------------------

..                              +-------------+
..               BmpMessage --> | bmp-tcp-out | - - - - > Proxied via TCP/IP
..                              +-------------+
