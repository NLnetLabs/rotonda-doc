File-based Configuration
========================

Rotonda 0.2 should normally run as a daemon, and a configuration file is
required using the ``-c`` option. This may change for future versions of Rotonda.

If you've installed Rotonda through a package manager, a simple configuration file is included in ``/etc/rotonda/rotonda.conf``.

If you've installed Rotonda with ``cargo install``, you will have to supply
a configuration yourself. Sample configurations can be found in the ``/etc``
directory of the `github repository of Rotonda <https://github.com/NLnetLabs/
rotonda/>`_.


The ``/etc/rotonda/rotonda.conf`` configuration file that comes with the
packaged version of Rotonada will listen to a router on all interfaces, on port 11019. You will probably want to edit that.


File Structure
==============

Global configuration happens in a file that by convention is
called ``rotonda[.DESCRIPTION].conf``, e.g. a there is file called
``rotonda.example.conf``, that describes an example configuration.

This file must be in `TOML format <https://toml.io/>`_ and is structured as
follows:

    - global settings
    - 1 or more connectors
    - 1 or more RIBs
    - 1 or more targets


Global Settings
===============

.. confval:: http_listen

    The "<IP ADDRESS>:<PORT>" to listen on for incoming HTTP requests.

.. confval:: response_compression (optional)

    Whether or not to GZIP compress responses if the client expresses support
    for it (via the HTTP "Accept-Encoding: gzip" request header). Set to false to
    completely disable GZIP response compression.

    Default: ``true``

.. confval:: log_level (optional)

    The detail level of the logging messages. This affects the number of log messages, as well as the detail within one message.

    possible values, in order of the leve of detail, are: [``"error"``, ``"warn"``, ``"info"``, ``"debug"``, ``"trace"``]

    Default: ``warn``

.. confval:: log_target (optional)

    The output that log messages are send to.

    Possible values are: [``stderr``, ``files``, ``syslog``]

    Default: ``stderr``

.. confval:: log_facility (optional)

    If the ``log_target`` is set to ``syslog``, this setting is used to set the facility used by the syslog mechanism.

    Possible values are: [ ``daemon`` ]

    Default: ``daemon``

.. confval:: log_file (optional)

    If the ``log_target`` is set to ``files``, this is the path to the file that is used to store log messages.

    Default: ``./rotonda.log``

