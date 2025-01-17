Reference
=========

This section describes the basic syntax of Roto scripts. This is written in
a reference-style. It is mostly meant as a cheatsheet, not as an introduction to
the language.

Comments
--------

Comments in Roto start with a ``#`` and end at the end of a line. They can
be inserted anywhere in the script and are ignored.

.. code-block:: roto

    # this is a comment

Block comments are not supported. To create a multiline comment, prefix every
line with a ``#``.

.. code-block:: roto

    # one comment line
    # another comment line

Literals
--------

Roto supports literals for primitive types:

- ``0``, ``1``, ``34``, ``-10``, ``0xFF`` etc. for integers
- ``true`` and ``false`` for booleans
- ``0.0.0.0``, ``2345:0425:2CA1:0000:0000:0567:5673:23b5``, ``0::``, etc.
  for IP addresses
- ``0.0.0.0/10`` for prefixes
- ``AS1234`` for AS numbers
- ``"Hello"`` for strings

Primitive types
---------------

There are several types at Roto's core, which can be expressed as literals.

- :roto:ref:`bool`: booleans
- :roto:ref:`u8`, :roto:ref:`u16`, :roto:ref:`u32`, :roto:ref:`u64`: unsigned integers of 8, 16, 32 and 64 bits, respectively
- :roto:ref:`i8`, :roto:ref:`i16`, :roto:ref:`i32`, :roto:ref:`i64`: signed integers of 8, 16, 32 and 64 bits, respectively
- :roto:ref:`IpAddr`: IP address
- :roto:ref:`Prefix`: prefixes
- :roto:ref:`Asn`: AS number
- :roto:ref:`String`: Strings

There are many more types available that have more to do with BGP. These are
described elsewhere. Note that Roto is case sensitive; writing the ``Asn`` type as
``ASN`` or ``asn`` won't work.

Integers
--------

As the previous section indicates, there are several types for integers in Roto.
This might be familiar to users of languages such as C and Rust, but not for
users of Python and similar languages which only have one integer type.

Roto is a compiled language and as such needs to know how many bytes to use for
a given integer. Hence, the number of bits are included in the type. The prefix
``u`` is used for unsigned (i.e. non-negative) numbers and ``i`` for signed integers.

Below is a table of all available integer types.

+-----------------+------+--------+----------------------------+----------------------------+
| Type            | Bits | Signed |                        Min |                        Max |
+=================+======+========+============================+============================+
| :roto:ref:`u8`  |    8 |     No |                          0 |                         255|
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`u16` |   16 |     No |                          0 |                     65,535 |
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`u32` |   32 |     No |                          0 |              4,294,967,295 |
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`u64` |   64 |     No |                          0 | 18,446,744,073,709,551,615 |
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`i8`  |    8 |    Yes |                       -128 |                         127|
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`i16` |   16 |    Yes |                     -32768 |                     65,535 |
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`i32` |   32 |    Yes |                -2147483648 |              4,294,967,295 |
+-----------------+------+--------+----------------------------+----------------------------+
| :roto:ref:`i64` |   64 |    Yes | -9,223,372,036,854,775,808 |  9,223,372,036,854,775,807 |
+-----------------+------+--------+----------------------------+----------------------------+

Arithmetic operators
--------------------

There are mathematical operators for common operations:

+-------+----------------+
| ``+`` | addition       |
+-------+----------------+
| ``-`` | subtraction    |
+-------+----------------+
| ``*`` | multiplication |
+-------+----------------+
| ``/`` | division       |
+-------+----------------+

These operators follow the conventional PEMDAS rule for precedence. The order is

- Parentheses
- Multiplication and division
- Addition and subtraction

Parentheses can always be used to force a certain order of operations. For
example, this expression:

.. code-block:: roto

    1 + 2 * 3    # evaluates to 7

is interpreted as

.. code-block:: roto

    1 + (2 * 3)  # evaluates to 7

and not as

.. code-block:: roto

    (1 + 2) * 3  # evaluates to 9

Comparison operators
--------------------

In addition to arithmetic operators, there are operators to compare values.
Comparison operators have a lower precedence than arithmetic operators. The
script won't compile if the operands have different types.

+--------+-----------------------+
| ``==`` | Equals                |
+--------+-----------------------+
| ``!=`` | Does not equal        |
+--------+-----------------------+
| ``>``  | Greater than          |
+--------+-----------------------+
| ``>=`` | Greater than or equal |
+--------+-----------------------+
| ``<``  | Less than             |
+--------+-----------------------+
| ``<=`` | Less than or equal    |
+--------+-----------------------+

Examples:

.. code-block:: roto

    5 > 10      # evaluates to false
    10 > 5      # evaluates to true
    5 == 5      # evaluates to true
    5 == true   # compile error!
    1 < x < 10  # compile error!

Logical operators
-----------------

Operators to combine boolean values are called logical operators. They have a
lower precedence than comparison operators. These are the logical operators in
Roto:

+---------+-------------+
| ``&&``  | Logical and |
+---------+-------------+
| ``||``  | Logical or  |
+---------+-------------+
| ``not`` | Negation    |
+---------+-------------+

Now that we have all the rules for precendence, here is an example using all types of
operators (arithmetic, comparison and logical):

.. code-block:: roto

    1 + x * 3 == 5 && y < 10

This is equivalent to:

.. code-block:: roto

    ((1 + (x * 3)) == 5) && (y < 10)

Strings
-------

Strings are enclosed in double quotes like so:

.. code-block:: roto

    "This is a string!"

Strings can be concatenated with ``+``:

.. code-block:: roto

    "race" + "car" # yields the string "racecar"

It also has some methods such as :ref:`String.contains` that can be very
useful. See the documentation for the :ref:`String` type for more
information.

If-else
-------

To conditionally execute some code, use an ``if`` block. The braces in the
example below are required. The condition does not require parentheses. The
condition must evaluate to a boolean.

.. code-block:: roto

    if x > 0 {
        # if the condition is true
    }

An ``else``-clause can optionally follow the ``if``-block. The ``if``-``else``
construct is an expression and therefore evaluates to a value.

.. code-block:: roto

    if x > 0 {
        # if the condition is true
    } else {
        # if the condition is false
    }

Functions
---------

Functions can be defined with the ``function`` keyword, followed by the name
and parameters of the function. It is required to specify the types of the
parameters. The return type is specified with ``->``. A function without a
return type does not return anything.

.. code-block:: roto

    function add_one(x: u64) -> u64 {
        x + 1
    }

This function can then be called like so:

.. code-block:: roto

    add_one(10)

A function can contain multiple expressions. The last expression is returned if
it is not terminated by a ``;``. The return can also be made explicit with the
``return`` keyword. This function is equivalent to the previous example. 

.. code-block:: roto

    function add_one(x: u64) -> u64 {
        return x + 1;
    }

The following function uses multiple statements to return ``0`` if the input is ``0``
and subtract ``1`` otherwise.

.. code-block:: roto

    function subtract_one(x: u64) -> u64 {
        if x == 0 {
            return 0;
        }
        x - 1
    }

This function does not return anything:

.. code-block:: roto

    function returns_nothing(x: u64) {
        x + 1;
    }

The ``return`` keyword can still be used in functions that don't return a value to
exit the function early.

When a function becomes more complex, intermediate results can be stored in local
variables with ``let``.

.. code-block:: roto

    function greater_than_square(x: i32, y: i32) {
        let y_squared = y * y;
        x > y_squared
    }

Filter-map
----------

A ``filter-map`` is a function that filters and transforms some incoming value.

Filter-maps resemble functions but they don't ``return``. Instead they
either ``accept`` or ``reject``, which determines what happens to the value.
Generally, as accepted value is stored or fed to some other component and a
reject value is dropped.

.. code-block:: roto

    filter-map reject_zeros(input: IpAddr) {
        if input == 0.0.0.0 {
            reject
        } else {
            accept
        }
    }

This describes a filter which takes in an IP address and accepts it if it is not
equal to ``0.0.0.0``.

Like with functions, intermediate results can be stored in variables with let
bindings.

.. code-block:: roto

    filter-map reject_zeros(input: IpAddr) {
        let zeros = 0.0.0.0;
        if input == zeros {
            reject
        } else {
            accept
        }
    }

A ``filter-map`` can also ``accept`` or ``reject`` with a value.

Anonymous records
-----------------

Multiple values can be grouped into records. A record is constructed with `{}`
and contains key-value pairs.

.. code-block:: roto

    { foo: 5, bar: 10 }

These records are statically typed, which means that records with different
field names or different field types are separate types. For example, this is
a type checking error:

.. code-block:: roto

    if x {
        { foo: 5, bar: 10 }
    } else {
        { foo: 5 }  # error!
    }

Note that this makes records significantly different from dictionaries in Python
and objects in JavaScript, which resemble hash-maps and are far more dynamic.

Fields of records can be accessed with the `.` operator.

.. code-block:: roto

    filter-map example_filter_map() {
        define {
            x = { foo: 5 };
        }
        apply {
            accept x.foo
        }
    }

Named records
-------------

Named records provide a more principled approach to grouping values which will
yield more readable type checking errors.

.. code-block:: roto

    type SomeRecord {
        foo: i32,
        bar: bool,
    }

    # ...

    x = SomeRecord { foo: 3, bar: false }

Roto checks that all declared values are provided and are of the same type.

There is an automatic coercion from anonymous records to named records:

.. code-block:: roto

    function foo(int: i32) -> SomeRecord {
        { foo: int, bar: false }  # implicitly coerced to SomeRecord
    }

Next steps
----------

You can learn more about Roto by looking at the documentation for the
:doc:`02_rotonda_std`.
