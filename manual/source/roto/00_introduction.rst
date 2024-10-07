Introduction
============

Roto is the filter language used by Rotonda. Here is an example filter written
in Roto:

.. code-block:: roto

    filter-map disallow_ip(message: BgpMessage) {
        apply {
            if message.ip() == 0.0.0.0 {
                reject
            } else {
                accept message
            }
        }
    }

Roto is a full programming language that is fast, safe and easy to use. It is
made to integrate especially well with Rotonda, so that writing filters is as
simple as possible. The scripts are a part of the configuration of Rotonda.

Scripts are compiled to machine code by Rotonda before they are executed. This
means that they run quickly and introduce minimal latency into your system.

A strong and static type system ensures that every expression must be of a well
defined, unambiguous type. Roto scripts therefore cannot crash Rotonda and can
be used safely. This does not mean that the user has to specify types
everywhere, most types can be inferred by the Roto compiler. When the compiler
detects a mistake in your script, it will emit a friendly message.

Roto has no facilities to create loops. The reason for this is that scripts 
need to run only for a short time and should not slow down the
application.

This chapter will guide you through using Roto for writing your scripts.
