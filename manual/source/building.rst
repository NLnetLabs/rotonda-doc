Building From Source
====================

.. warning::

   Building from source is perfectly possible, but you have to ensure all the
   required configuration files to run Rotonda are in the right place.
   If you intend to follow the `Quick Tour`, it is recommend to use a packaged
   version if possible.

   If you do build from source but run into problems afterwards, refer to
   :doc:`/configuration`.



In addition to meeting the :ref:`system requirements <installation:System
Requirements>`, these are two things you need to build Rotonda: 

- a C toolchain
- Rust

You can run Rotonda on any operating system and CPU architecture where you
can fulfil these requirements.

Dependencies
------------

Some of the libraries used by Rotonda require a C toolchain, most notably the
MQTT client. You also need Rust because that’s the programming language that
Rotonda has been written in.

C Toolchain
"""""""""""

Some of the libraries Rotonda depends on require a C toolchain to be present.
Your system probably has some easy way to install the minimum set of packages
to build from C sources. For example, this command will install everything you
need on Debian/Ubuntu, provided the currently logged in user has enough
privileges to install system packages:

.. code-block:: text

  $ sudo apt install curl build-essential gcc make

If you are unsure, try to run :command:`cc` on a command line. If there is a
complaint about missing input files, you are probably good to go.

.. _rustup:

Rust
""""

The Rust compiler runs on, and compiles to, a great number of platforms,
though not all of them are equally supported. The official `Rust Platform
Support`_ page provides an overview of the various support levels.

While some system distributions include Rust as system packages, Rotonda
relies on a relatively new version of Rust, currently 1.71.0 or newer. We
therefore suggest to use the canonical Rust installation via a tool called
:program:`rustup`.

Assuming you already have :program:`curl` installed, you can install
:program:`rustup` and Rust by simply entering:

.. code-block:: text

  $ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

This will install the stable rust toolchain, on a per user basis. This means
that you probably want to install this as the same user as you will be running
the Rotonda application itself. This should most probably be a non-root
user, so we suggest you create a `rotonda` user, log in as that user and then
perform the `curl` command above.

Make sure to restart your shell, or add `$HOME/.cargo/bin` to your $PATH
enviroment variable manually. This will make sure that the tools, most notably
`cargo`, are reachable without specifying the full path.

Alternatively, visit the `Rust website
<https://www.rust-lang.org/tools/install>`_ for other installation methods.

Building and Updating
---------------------

In Rust, a library or executable program such as Rotonda is called a
*crate*. Crates are published on `crates.io
<https://crates.io/crates/rotonda>`_, the Rust package registry. Cargo is
the Rust package manager. It is a tool that allows Rust packages to declare
their various dependencies and ensure that you’ll always get a repeatable
build. 

Cargo fetches and builds Rotonda’s dependencies into an executable binary
for your platform. By default you install from crates.io, but you can for
example also install from a specific Git URL, as explained below.

Installing the latest Rotonda release from crates.io is as simple as
running:

.. code-block:: bash
  :substitutions:

  $ cargo install rotonda --version |version| --locked

The command will build Rotonda and install it in the same directory that Cargo
itself lives in, likely ``$HOME/.cargo/bin``. This means Rotonda will be in
your path, too. The version of Rotonda that was build corresponds to the
version of this documentation you are reading. If for any reason you want to
install another version of Rotonda, you should substitute the value after
``--version`` with the version you want. Omitting the whole ``--version```
option will install the latest published version on ``crates.io``.

.. _download-config:

Downloading the configuration files
"""""""""""""""""""""""""""""""""""

Although Rotonda has a built-in configuration, and you can create a
configuration file from scratch it's very useful to download the configuration
files that come with Rotonda. These files are situated in the github
repository of Rotonda. Provided you have a version of `git` higher than or
equal to 2.25 installed, you can issue these commands to download them to a
newly created directory, called ``rotonda`` in your current working directory:

.. code-block:: bash
  :substitutions:

  $ git clone --no-checkout --depth 1 --branch v|version| https://github.com/nlnetlabs/rotonda && cd rotonda/ && git sparse-checkout set etc && git checkout v|version|

Again, the version of the configuration files installed here matches with the
Rotonda version you just installed, and this documentation. If you've
installed another Rotonda version, you should also substitute the two version
values with the version you used when installing Rotonda.

Updating
""""""""

If you want to update to the latest version of Rotonda, it’s recommended
to update Rust itself as well, using:

.. code-block:: bash

  $ rustup update

Use the ``--force`` option to overwrite an existing version with the latest
Rotonda release:

.. code-block:: text

  $ cargo install --locked --force rotonda

Installing Rotonda from the main branch
"""""""""""""""""""""""""""""""""""""""

All new features of Rotonda are built on a branch and merged via a `pull
request <https://github.com/NLnetLabs/rotonda/pulls>`_, allowing you to
easily try them out using Cargo. If you want to try a specific branch from
the repository you can use the ``--git`` and ``--branch`` options:

.. code-block:: text

  $ cargo install --git https://github.com/NLnetLabs/rotonda.git --branch main

Note that you will also have to download the correct configuration files with:

.. code-block:: bash

  $ git clone --no-checkout --depth 1 --branch main https://github.com/nlnetlabs/rotonda && cd rotonda/ && git sparse-checkout set etc && git checkout main

.. Seealso:: For more installation options refer to the `Cargo book
             <https://doc.rust-lang.org/cargo/commands/cargo-install.html#install-options>`_.

Platform Specific Instructions
------------------------------

For some platforms, :program:`rustup` cannot provide binary releases to
install directly. The `Rust Platform Support`_ page lists
several platforms where official binary releases are not available, but Rust
is still guaranteed to build. For these platforms, automated tests are not
run so it’s not guaranteed to produce a working build, but they often work to
quite a good degree.

.. _Rust Platform Support:  https://doc.rust-lang.org/nightly/rustc/platform-support.html

OpenBSD
"""""""

On OpenBSD, `patches
<https://github.com/openbsd/ports/tree/master/lang/rust/patches>`_ are
required to get Rust running correctly, but these are well maintained and
offer the latest version of Rust quite quickly.

Rust can be installed on OpenBSD by running:

.. code-block:: bash

  $ pkg_add rust
