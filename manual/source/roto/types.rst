Block ``filter``
================

A ``filter`` block represents a filter that Rotonda will invoke in a Rib or
Connector Unit, as specified in the :doc:`configuration
</config/introduction>` file of Rotonda.

A filter will be run for each payload that Rotonda receives in the unit where
the filter is installed. The filter can access that payload and it must return
a ``filtering decision``. A filtering decision is either a ``accept`` or a
``reject`` expression.

The body of a ``filter`` block must contain only sections. It must contain
exactly one ``define`` section, and exactly one ``apply`` section. Optionally
it may contain one or more ``term`` sections and one or more ``action``
sections.

Section ``define``
-------------------

A ``define`` section in a ``filter`` contains all the variable declarations
and assignments that can be used through-out the ``filter`` block. It must
contain at least one declaration, and that is the declaration of the payload
to a type and variable name, like so:

.. code:: text

    define {
        rx msg: BmpMessage;
    }

The Roto ``rx`` expression is used to define the declaration of the payload.
It is followed by the variable name that can be used to refer to it
through-out the ``Roto`` script. The name is followed by a colon and the type
of the payload. So, in this example we are referring to the payload with the
variable name ``msg`` and its type is ``BmpMessage``.

Section ``term``
----------------

Section ``action``
------------------

Section ``apply``
-----------------

Block ``filter-map``
====================

Block ``rib``
=============

Block ``table``
===============

Block ``output-stream``
=======================

