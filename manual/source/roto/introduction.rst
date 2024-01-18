Introduction
============

``Roto`` is the filter language used by Rotonda. Eventually it will also be used
as a query and configuration language.

``Roto`` is a strongly typed, compiled language, i.e. every expression has to
return a value that is an instance of a well defined, unambiguous type.
Variable assignments, Constant definitions and method invocations are all
expressions in ``Roto``. This does not mean that the user has to specify types
everywhere, most types can be inferred by the ``Roto`` compiler. Next to that
Roto allows for automatic type conversions where possible. ``Roto`` has a fair
amount of builtin types, both generic ones, e.g. unsigned 32-bits integers
(``U32``), strings, etc, and types specific to BGP and routing, e.g. it has a
``Prefix`` type, a ``AsPath`` type and even a ``Route`` type. ``Roto`` also
has the compound types, ``List`` and ``Record``. Users can create their own
types based on these two types.

``Roto`` has no facilities for users to create loops of any kind. This is on
purpose, and the reasoning behind this is similar to embedded languages like
`eBPF <https://ebpf.io/what-is-ebpf/>`_. The host application, in our case
Rotonda, and in the eBPF case the Linux kernel, needs to be sure that the
embedded program will actually finish and return a value, and in a reasonable
- maybe even predictable - timeframe. As such, ``Roto`` aims to be non-turing
complete.

The ``Roto`` toolchain consists of a compiler and a virtual machine, both of
which are embedded in the ``Rotonda`` application. This means that the only
requirements to create filters from source code is a running Rotonda instance.
``Roto`` does not rely on Rust or any part of its toolchain. The compiler
takes ``Roto`` source code and compiles it down to a so-called `Mid-level
Intermediate Representation` (``MIR``). This MIR code is then fed by Rotonda
into a virtual machine. This MIR code is then executed by the virtual machine.
The virtual machine itself consists of a stack machine and a bunch of
registers.

The Future
----------

In the future the virtual machine will probably will take a low-level IR, to
facilate running user-created plug-ins, written in a general purpose language
of the user's choice. These plug-ins would allow users to create more complex,
turing-complete programs. Rotonda can compile, load MIR Code, and execute the
code in virtual machines transparant to the user, and as a consequence the
user can create, modify and remove Roto filter on-the-fly in a running Rotonda
system.
