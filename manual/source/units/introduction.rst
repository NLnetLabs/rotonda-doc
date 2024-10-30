introduction
------------

A Rotonda application consists of multiple units strung together into a
pipeline. Currently Rotonda has features two types of units: Connector Units
and RIB units.

Units

Connector Units
===============

Connectors are units that allow data to flow into a Rotonda application.
Currently Rotonda supports three different types of connectors. Connectors
can start and maintain sessions with other systems. Connectors therefore can
keep state.

BMP Connector: `bmp-tcp-in`
===========================

The BMP connector enables Rotonda to initiate a BMP connection to a Router,
where Rotonda acts as BMP station.

Configuration Options
---------------------

`````{roto:type} listen


bgp-tcp-in

mrt-in


Rib Units
========

rib Physical RIB

rib (virtual RIB)


Target
=======

mqtt-out

null-out

