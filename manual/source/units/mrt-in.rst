mrt-in `(experimental)`
======================

This unit can take one or several ``mrt`` files (:RFC:`6396`) and emulate an
open BGP session with the contents of the table dumps in it.

It will load all the RIB entries and load them into a Rotonda RIB. Routes will
be stored per peer.

.. confval:: type (mandatory)

	This must be set to `mrt-in` for this type of connector.

.. confval:: filename (mandatory)

	The path to the ``mrt`` file containing one or more table dump entries, that will be loaded into the receiving RIB.
