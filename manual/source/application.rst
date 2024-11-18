Pipeline
========

A Rotonda application consists of multiple components strung together into a
pipeline. Currently Rotonda features three different types of components: Connectors, RIB and Targets.

Data flows from West to East beginning with a connector, through
one or more intermediate ribs and out terminating at at least one target.

Additionally Rotonda has HTTP interfaces to the North and output stream
interfaces to the South. The HTTP interfaces to the North may be used to
inspect and interact with the application. a RIB extends the HTTP interface
with additional capabilities. The target to the South provide support for
alternate forms of output such as MQTT event publication and logging/capture
to file.

Taken together one can think of the flow of information like so:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
	                             (North)
	                             HTTP/API
	                               │ ▲
	                               │ │
	                      ┌────────▼─┴────────┐
	(West) Connector ─●───▶        RIB        │───▶ Null Target (East)
	                  │   └─────────┬─────────┘
	       Connector ─┘             │
	                                ▼
	                       Optional MQTT Target
	                             (South)
	</pre>

Some type of connectors and all RIBs have programmable *roto* filters built
into them.

Components
==========

A Connector is a component that connects Rotonda to an external source of
BGP data. This may currently be a BGP speaker (a router through a peering
session), a BMP monitored router, or one of multiple MRT files. Rotonda
requires at least one connector to be present. The ``bmp-tcp-in`` and the ``bgp-tcp-in`` connector types have a programmable :doc:`Roto </roto/introduction>` filter built in.

A RIB is situated at an intermediate stage in the Rotonda pipeline and also
has a :doc:`Roto </roto/introduction>` programmable filter in front of it. It
allows users to filter, transform and store BGP (and related) data.

A Target is a component that is situated at a final output stage in Rotonda,
it will output BGP data to an external system. Rotonda requires at least one
target to be present.

Each component is able to process certain types of input and emit certain
types of output. More information about each component type is given in the
next sections.

Definition & Configuration
--------------------------

All components have their own section in the configuration file and names
must be unique, types must be valid and any mandatory settings specific to the
component type must be specified. Components are included in the
pipeline by setting the ``sources`` field inside the receiving component to
include the name of the sending component.
