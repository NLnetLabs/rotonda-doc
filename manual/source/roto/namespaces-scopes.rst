Structure and scoping
=====================

Structure
---------

The top-level of a ``Roto`` script can contain
definitions of blocks. The type of these blocks can be:

- ``filter-map``
- ``filter``
- ``rib``
- ``table``
- ``output-stream``

The syntax for all definitions of blocks looks like this:

.. code:: text

    filter my-filter { }

In this example, the type of the block is ``filter``, the name is `my-filter`,
and its body (the code between the curly braces) is empty.

The top-level can also contain type definitions for user-defined types. These
look very similar to block definitions:

A type definition looks like this:

.. code:: text

    type MyRec {
        asn: Asn
    }

Im this example, a type with the name ``MyRec`` is created, and is defined as
`Record` with a field called ``asn``, which is of type ``Asn``.

Lastly, the top-level can contain single-line comments. Comments start with
``//``.

Roto Global namespace and Block Scopes
--------------------------------------

For now, ``Roto`` only has one namespace, namely the Global namespace. Rotonda
loads all available `Roto` source code from all files in a directory on the
local file system specified in a Rotonda :doc:`configuration
</config/introduction>` file and puts all that source code in said global
namespace. For the roto user this means that all identifiers, i.e. names of
blocks, in the top-level of all loaded scripts must be unique across all
these files. A failure to do so will result in a compilation error, and the
compilation process will abort.

Although ``Roto`` only has one namespace, it does have multiple scopes. It has
a global scope, which lives in the global namespace. All built-in types and
user-defined types are situated in this global scope. Moreover, some constants
are defined in the global namespace. All other scopes are nested inside the
global scope, and nothing that is defined in the global scope with a name
("identifier"), be it block definitions, or type definitions, or constants,
or built-in types, can be redefined ("shadowed") in the nested scopes. An
attempt to do so will result in a compilation error, and the compilation
process will be aborted.

Each block defined in the global namespace will have its own nested scope in
its body. This means that a variable assignment in one block has no effect
whatsoever on other blocks.

Consider this example:

.. code:: text
    
    // Global Scope is active here

    filter a {
        // Nested Scope for filter a is active here
        define {
            pfx = 192.0.2.0/24;
            my_rec = MyRec {
                asn: 65534,
                prefix: pfx
            };
        }
    }

    filter b {
        // Nested Scope for filter b is active here
        define {
            pfx = 192.0.3.0/24;
            my_rec = MyRec {
                asn: 65535,
                prefix: pfx
            };
        }
    }

    // Global Scope is active here
    type MyRec {
        asn: Asn,
        prefix: Prefix,
    }

In this example we defined a type ``MyRec``. That type is defined in the
global scope and is therefore usable in all scopes. So in the nested scopes of
filter a and filter b we can create new instances of this type. Filter a and
filter b use the same variable names while creating these instances, but that
does not matter: they are scoped to their own block, so they don't interfere.
