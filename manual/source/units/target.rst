Targets
=======

mqtt-out
--------

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

Configuration Options
---------------------

The ``mqtt-out`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[target.<NAME>]
	type = "mqtt-out"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.

.. confval:: type (mandatory)

	This must be set to ``mqtt-out`` for this type of target.
	
.. confval:: sources (mandatory)

	An ["array", "of", "upstream", "unit", "names"] from which data will be
	received.

.. confval:: destination (mandatory)

	A "host:port" string specifying the host or IP address of an MQTT broker
	to connect to. If the ":port" part is omitted the IANA registered MQTT port
	number [3] 1883 will be used. Note: Only unencrypted TCP connections are
	supported, i.e. TLS and WS are not supported.

.. confval:: cliend_id (optional)

	A unique name to identify the client to the server in order to hold state
	about the session. If empty the server will use a clean session and assign a
	random name to the client. Servers are required to support names upto 23 bytes
	in length but may support more.

Default: ""

.. confval:: qos (optional)

	MQTT quality-of-service setting for determining how many times a message can
	be delivered:

	- 0 (at most once)
	- 1 (at least once)
	- 2 (exactly once)

	Higher values require more synchronization with the broker leading to lower
	throughput but greater reliability/correctness.

Default: 2

.. confval:: queue_size (optional)

	The number of messages that can be buffered for delivery to the MQTT broker.

	Default: 1000

.. confval:: connect_retry_secs (optional)

	The number of seconds to wait before attempting to reconnect to the MQTT
	broker if the connection is lost.

	Default: 60

.. confval:: publish_max_secs (optional)

	The number of seconds to wait before timing out an attempt to publish a
	message to the MQTT broker.

	Default: 5

.. confval:: topic_template (optional)

	A "string" template that will be used to determine the MQTT topic to which
	events will be published. If present, the "{id}" placeholder will be replaced
	by the "topic" value in the incoming Record value. When using "{id}" an
	MQTT client that supports MQTT wildcards can still receive all events by
	subscribing to 'rotonda/#' for example.

Default: "rotonda/{id}"

.. confval:: username (optional)

	A "string" username for login to the MQTT broker.

.. confval:: password (optional)

	A "string" password for login to the MQTT broker.

null-out
--------

This target discards everything it receives.

Rotonda requires that there always be at least one target. Using this target
allows you to run Rotonda without any output at the east-side of the pipeline.

Configuration Options
---------------------

The ``null-out`` component can be defined in the Rotonda configuration file,
like this:

.. code-block:: text

	[target.<NAME>]
	type = "null-out"
	..

where ``<NAME>`` is the name of the component, to be referenced in the value
of the ``sources`` field in a receiving component.

.. confval:: type (mandatory)

	This must be set to `null-out` for this type of target.

.. confval:: source (mandatory)

	The upstream unit from which data will be received.
