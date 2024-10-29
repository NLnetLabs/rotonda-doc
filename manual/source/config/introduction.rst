Introduction
------------

Built-in vs file-based configuration
------------------------------------

When Rotonda is compiled, a configuration is built in. The built-in
configuration is used when no configuration file is specified when invoking
``rotonda`` on the command line with the ``-c`` option. You can see the
details of the built-in configuration by issuing ``rotonda
--print-config-and-exit`` on the command line.

If you've installed Rotonda through a binary package, the built-in
configuration is roughly equivalent to the file you will find in
``/etc/rotonda/rotonda.conf``.

When running with the built-in configuration Rotonda will look for the roto
filter scripts in the absolute path ``/etc/rotonda/filters/``. If that
directory can not be found, or the required filters cannot be found in that
path, no filter scripts can be loaded resulting in a filter-less,
accept-everything Rotonda instance.

In contrast: if you are starting Rotonda with an explicit configuration file,
by invoking the ``-c`` option, and the ``roto_scripts_path`` in that
configuration file cannot be found, or the required filters cannot be found,
then **Rotonda will not start**.

.. tip::

    the built-in configuration and the configuration files included in the
    package will look in the absolute path ``/etc/rotonda/filters/`` by
    default.

.. tip::

    When compiling from source, the file in the repository in
    ``etc/rotonda/rotonda.builtin.conf`` is used to create the built-in
    configuration. Note that if you comment out the ``[targets.mqtt]`` section,
    mqtt functionality will not be available in the Rotonda build you are going
    to compile based on it.

    This only applies to building with ``cargo build --release``, not ``cargo
    install``.

Completing the configuration file
---------------------------------

The ``/etc/rotonda/rotonda.conf`` configuration file that comes with the
packaged version of Rotonda is not complete, and Rotonda will abort if you try
to use it as-is.  You will have to edit it and at the very least fill out the
values in the ``[targets.mqtt]`` section. Probably you'll also want to edit the
fields ``my_asn`` and ``my_bgp_id`` in the ``[units.bgp-in]`` section. 

