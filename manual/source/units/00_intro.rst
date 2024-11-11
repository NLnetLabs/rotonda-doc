Introduction
------------

A Rotonda application consists of multiple units strung together into a
pipeline. Currently Rotonda features two types of units: Connector Units
and RIB units. Next to that, Rotonda also has targets, current types are
`mqtt-out` and `null-out`. Colectively, units and targets are referred to
as components.

Data flows from West to East beginning with at least one input unit, through
zero or more intermediate units and out terminating at at least one target.

Additionally Rotonda has HTTP interfaces to the North and output stream
interfaces to the South. The HTTP interfaces to the North may be used to
inspect and interact with the application. Some types of units and target
extend the HTTP interface with additional capabilities. The output stream
interfaces to the South provide support for alternate forms of output such
as MQTT event publication, logging/capture to file and proxying to external
parties.

Taken together one can think of the flow of information like so:

.. raw:: html

    <pre style="font-family: menlo; font-weight: 400; font-size:0.75em;">
                                 (North)
                                HTTP APIs
                                   ^ |
                                   | |
                                   | v
       (West) BGP/BMP inputs --> pipeline --> Null target (East)
                                    |
                                    |
                                    v
                            Optional MQTT outputs
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
