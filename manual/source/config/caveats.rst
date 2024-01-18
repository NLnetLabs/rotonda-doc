.. _config-caveats:

Important Caveats
=================

The current configuration approach of Rotonda can be counter-intuitive and is
likely to change in the near future. While you might not encounter any problems
when using Rotonda from packaged sources (such as the `.debs` and `.rpms`) and
running it via the provided service files, building from source and/or running
Rotonda by hand might result in some unexpected outcomes.


Embedded vs file-based configuration
------------------------------------

When Rotonda is compiled, a default configuration is embedded. This
configuration is **almost** equal to what is copied to e.g.
``/etc/rotonda/rotonda.conf`` when installing a package. The embedded
configuration is used when no configuration file is explicitly passed to the
``rotonda`` binary on the command line via the ``-c`` option.


An important difference between the embedded default configuration, and the one
copied to ``/etc`` is the ``roto_scripts_path`` parameter. In the embedded
configuration, that parameter is set to ``etc/``, a path relative to the working
directory. In other words, there should be a subdirectory ``etc`` in the
directory you run  ``rotonda`` from.

If the directory specified by ``roto_scripts_path`` can not be found, no filter
scripts can be loaded resulting in a filter-less, accept-everything Rotonda
instance.


Compile-time effecting parameters
---------------------------------

When compiling from source, depending on the exact contents of the
``rotonda.builtin.conf`` file, some features might be omitted from the build.
This currently mainly concerns MQTT functionality.

