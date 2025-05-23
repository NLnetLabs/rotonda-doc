System Requirements
-------------------

The system requirements of Rotonda depend highly on the volume of routes that
you want to keep in memory, and the amount of BGP/BMP messages that flow
through Rotonda. If you do not wish to keep any routes in memory (say you want
to emit only MQTT messages based on incoming messages), the requirements would
be fairly minimal, both in terms of memory and CPU power. If on the other
hand, you want to keep all routes that you receive from multiple sessions that
feed full tables, your memory requirements will surely run into the tens of
gigabytes.

Binary Packages
---------------

Rotonda is packaged for several popular Linux distributions, and Docker images
based on Alpine Linux are provided. Instructions for all these are below.

You can also build Rotonda from the source code using Cargo, Rust's build
system and package manager. Cargo lets you build Rotonda on almost any operating
system and CPU architecture. Refer to the :doc:`building` section to get
started.

.. tabs::

   .. group-tab:: Debian

       To install a Rotonda package, you need the 64-bit version of one of
       these Debian versions:

         -  Debian Bookworm 12
         -  Debian Bullseye 11
         -  Debian Buster 10

       These Packages are all available for the ``amd64``/``x86_64`` and
       ``arm64``/``aarch64`` architectures.
       
       First update the :program:`apt` package index: 

       .. code-block:: bash

         $ sudo apt update

       Then install packages to allow :program:`apt` to use a repository over HTTPS:

       .. code-block:: bash

         $ sudo apt install curl gpg

       Add the GPG key from NLnet Labs:

       .. code-block:: bash

         $ curl -fsSL https://packages.nlnetlabs.nl/aptkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/nlnetlabs-archive-keyring.gpg

       Now, use the following command to set up the *main* repository:

       .. code-block:: bash

          $ echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/nlnetlabs-archive-keyring.gpg] https://packages.nlnetlabs.nl/linux/debian \
          $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/nlnetlabs.list > /dev/null

       Update the :program:`apt` package index once more: 

       .. code-block:: bash

          $ sudo apt update

       You can now install Rotonda with:

       .. code-block:: bash

          $ sudo apt install rotonda

       After installation Rotonda will run immediately as the user
       *rotonda* and be configured to start at boot. 
       
       You can check the status of Rotonda with:
       
       .. code-block:: bash 
       
          $ sudo systemctl status rotonda
       
       You can view the logs with: 
       
       .. code-block:: bash
       
          $ sudo journalctl --unit=rotonda

   .. group-tab:: Ubuntu

       To install a Rotonda package, you need the 64-bit version of one of
       these Ubuntu versions:

         - Ubuntu Jammy 22.04 (LTS)
         - Ubuntu Focal 20.04 (LTS)
         - Ubuntu Bionic 18.04 (LTS)

       Packages are available for the ``amd64``/``x86_64`` architecture only.
       
       First update the :program:`apt` package index: 

       .. code-block:: bash

          $ sudo apt update

       Then install packages to allow :program:`apt` to use a repository over HTTPS:

       .. code-block:: bash

          $ sudo apt install \
            ca-certificates \
            curl \
            gnupg \
            lsb-release

       Add the GPG key from NLnet Labs:

       .. code-block:: bash

          $ curl -fsSL https://packages.nlnetlabs.nl/aptkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/nlnetlabs-archive-keyring.gpg

       Now, use the following command to set up the *main* repository:

       .. code-block:: bash

          $ echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/nlnetlabs-archive-keyring.gpg] https://packages.nlnetlabs.nl/linux/ubuntu \
          $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/nlnetlabs.list > /dev/null

       Update the :program:`apt` package index once more: 

       .. code-block:: bash

          $ sudo apt update

       You can now install Rotonda with:

       .. code-block:: bash

          $ sudo apt install rotonda

       After installation Rotonda will run immediately as the user
       *rotonda* and be configured to start at boot.
       
       You can check the status of Rotonda with:
       
       .. code-block:: bash 
       
          $ sudo systemctl status rotonda
       
       You can view the logs with: 
       
       .. code-block:: bash
       
          $ sudo journalctl --unit=rotonda

   .. group-tab:: RHEL/CentOS

       To install a Rotonda package, you need Red Hat Enterprise Linux
       (RHEL) 7 or 8, or compatible operating system such as Rocky Linux.
       Packages are available for the ``amd64``/``x86_64`` architecture only.
       
       First create a file named :file:`/etc/yum.repos.d/nlnetlabs.repo`,
       enter this configuration and save it:
       
       .. code-block:: text
       
          [nlnetlabs]
          name=NLnet Labs
          baseurl=https://packages.nlnetlabs.nl/linux/centos/$releasever/main/$basearch
          enabled=1
        
       Add the GPG key from NLnet Labs:
       
       .. code-block:: bash
       
          $ sudo rpm --import https://packages.nlnetlabs.nl/aptkey.asc
       
       You can now install Rotonda with:

       .. code-block:: bash

          $ sudo yum install -y rotonda

       After installation Rotonda will run immediately as the user
       *rotonda* and be configured to start at boot. 
       
       You can check the status of Rotonda with:
       
       .. code-block:: bash 
       
          $ sudo systemctl status rotonda
       
       You can view the logs with: 
       
       .. code-block:: bash
       
          $ sudo journalctl --unit=rotonda
       
   .. group-tab:: Docker

       Rotonda Docker images are built with Alpine Linux. The supported 
       CPU architectures are shown on the `Docker Hub Rotonda page 
       <https://hub.docker.com/r/nlnetlabs/rotonda/tags>`_ per Rotonda
       version (aka Docker "tag") in the ``OS/ARCH`` column.

Updating
--------

.. tabs::

   .. group-tab:: Debian

       To update an existing Rotonda installation, first update the 
       repository using:

       .. code-block:: bash

          $ sudo apt update

       You can use this command to get an overview of the available versions:

       .. code-block:: bash

          $ sudo apt policy rotonda

       You can upgrade an existing Rotonda installation to the latest
       version using:

       .. code-block:: bash

          $ sudo apt --only-upgrade install rotonda

   .. group-tab:: Ubuntu

       To update an existing Rotonda installation, first update the 
       repository using:

       .. code-block:: bash

          $ sudo apt update

       You can use this command to get an overview of the available versions:

       .. code-block:: bash

          $ sudo apt policy rotonda

       You can upgrade an existing Rotonda installation to the latest
       version using:

       .. code-block:: bash

          $ sudo apt --only-upgrade install rotonda

   .. group-tab:: RHEL/CentOS

       To update an existing Rotonda installation, you can use this
       command to get an overview of the available versions:
        
       .. code-block:: bash
        
          $ sudo yum --showduplicates list rotonda
          
       You can update to the latest version using:
         
       .. code-block:: bash
         
          $ sudo yum update -y rotonda
             
   .. group-tab:: Docker

       Assuming that you run Docker with image `nlnetlabs/rotonda`, upgrading
       to the latest version can be done by running the following commands:
        
       .. code-block:: bash
       
          $ sudo docker pull nlnetlabs/rotonda
          $ sudo docker rm --force rotonda
          $ sudo docker run <your usual arguments> nlnetlabs/rotonda


Installing Specific Versions
----------------------------

Before every new release of Rotonda, one or more release candidates are 
provided for testing through every installation method. You can also install
a specific version, if needsed

.. tabs::

   .. group-tab:: Debian

       If you would like to try out release candidates of Rotonda you can add
       the *proposed* repository. This repository can live side by side with
       the *main* repository.
       
       If you have already installed the *main*
       repository you can skip the first three steps here, and go directly to
       `Debian proposed repository`_.
       
       First update the :program:`apt` package index: 

       .. code-block:: bash

         $ sudo apt update

       Then install packages to allow :program:`apt` to use a repository over HTTPS:

       .. code-block:: bash

         $ sudo apt install curl gpg

       _`Add the GPG key` from NLnet Labs:

       .. code-block:: bash

          curl -fsSL https://packages.nlnetlabs.nl/aptkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/nlnetlabs-archive-keyring.gpg

       Now, use the following command to set up the _`Debian proposed repository`:

       .. code-block:: bash

          echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/nlnetlabs-archive-keyring.gpg] https://packages.nlnetlabs.nl/linux/debian \
          $(lsb_release -cs)-proposed main" | sudo tee /etc/apt/sources.list.d/nlnetlabs-proposed.list > /dev/null

       Make sure to update the :program:`apt` package index:

       .. code-block:: bash

          $ sudo apt update
       
       You can now use this command to get an overview of the available 
       versions:

       .. code-block:: bash

          $ sudo apt policy rotonda

       You can install a specific version using ``<package name>=<version>``,
       e.g.:

       .. code-block:: bash

          $ sudo apt install rotonda=0.2.0~rc2-1buster

   .. group-tab:: Ubuntu

       If you would like to try out release candidates of Rotonda you can
       add the *proposed* repository to the existing *main* repository
       described earlier. 
       
       Assuming you already have followed the steps to install regular
       releases, run this command to add the additional repository:

       .. code-block:: bash

          $ echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/nlnetlabs-archive-keyring.gpg] https://packages.nlnetlabs.nl/linux/ubuntu \
          $(lsb_release -cs)-proposed main" | sudo tee /etc/apt/sources.list.d/nlnetlabs-proposed.list > /dev/null

       Make sure to update the :program:`apt` package index:

       .. code-block:: bash

          $ sudo apt update
       
       You can now use this command to get an overview of the available 
       versions:

       .. code-block:: bash

          $ sudo apt policy rotonda

       You can install a specific version using ``<package name>=<version>``,
       e.g.:

       .. code-block:: bash

          $ sudo apt install rotonda=0.2.0~rc2-1bionic
          
   .. group-tab:: RHEL/CentOS

       To install release candidates of Rotonda, create an additional repo 
       file named :file:`/etc/yum.repos.d/nlnetlabs-testing.repo`, enter this
       configuration and save it:
       
       .. code-block:: text
       
          [nlnetlabs-testing]
          name=NLnet Labs Testing
          baseurl=https://packages.nlnetlabs.nl/linux/centos/$releasever/proposed/$basearch
          enabled=1
        
       You can use this command to get an overview of the available versions:
        
       .. code-block:: bash
        
          $ sudo yum --showduplicates list rotonda
          
       You can install a specific version using 
       ``<package name>-<version info>``, e.g.:
         
       .. code-block:: bash
         
          $ sudo yum install -y rotonda-0.2.0~rc2
             
   .. group-tab:: Docker

       All release versions of Rotonda, as well as release candidates and
       builds based on the latest main branch are available on `Docker Hub
       <https://hub.docker.com/r/nlnetlabs/rotonda/tags?page=1&ordering=last_updated>`_. 
       
       For example, installing Rotonda 0.2.0 RC2 is as simple as:
        
       .. code-block:: bash
       
          $ sudo docker run <your usual arguments> nlnetlabs/rotonda:v0.2.0-rc2
               
