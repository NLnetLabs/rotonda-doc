.. _troubleshooting :

Unable to load Roto scripts
===========================

Upon starting Rotonda, an error similar to the one below is printed:

.. code-block:: text

	Unable to load Roto scripts: 
	read directory error for path /Users/jasper/Projects/rotonda/etc/filters: 
	No such file or directory (os error 2).
	Roto filters 'rib-in-post-filter', 'bmp-in-filter', 'bgp-in-filter', 
	'rib-in-pre-filter' are referenced by your configuration but do not exist
	because no .roto scripts could be loaded from the configured
	`roto_scripts_path` directory '/etc/rotondafilters'. These filters will be ignored.


This is likely to happen when running ``rotonda`` by hand from a shell (as
opposed to running it as a service after installing it from a package),
without specifying a configuration file (with the ``-c`` option). In that case
Rotonda falls back to the built-in configuration. This configuration expects
to find specific filters in the absolute path ``/etc/rotonda/``.

To obtain the required configuration files, refer to :ref:`download-config`.
