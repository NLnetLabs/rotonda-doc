File-based Configuration
------------------------------------

Rotonda 0.2 should normally run as a deamon, and a configuration file is
required using the ``-c`` option. This may change for future versions of Rotonda.

If you've installed Rotonda through a package manager, a simple configuration file is included in ``/etc/rotonda/rotonda.conf``.

If you've installed Rotonda with `cargo install`, you will have to supply a configuration yourself.

Editing the default File
------------------------

The ``/etc/rotonda/rotonda.conf`` configuration file that comes with the
packaged version of Rotonada will listen to a router on all interfaces, on port 11019. You will probably want to edit that.


File Structure
--------------

Global configuration happens in a file that by convention is
called ``rotonda[.DESCRIPTION].conf``, e.g. a there is file called
``rotonda.example.conf``, that describes an example configuration.

This file must be in TOML format (https://toml.io/) and is structured as
follows:

    - global settings
    - 1 or more units
    - 1 or more targets
