# ArcticStack

**ArcticStack** is a software stack which aims to provide Ansible Collections,
playbooks and tools to deploy and manage HPC and AI clusters based on RHEL-like
operating systems.

This project is a fork of [BlueBanquise](https://bluebanquise.com) 1.4.0.
BlueBanquise supports a wider range of operating systems and has a simpler
implementation of Ansible roles which target teaching purposes. The name
Arctic is a wink to BlueBanquise.

## Documentation

Currently, the documentation is available upstream on the [BlueBanquise
website](https://bluebanquise.com/documentation/).

## Packages

The stack relies on some packages not available in the OS distribution or in
EPEL. Such packages are built and made available upstream at [BlueBanquise
repositories](https://bluebanquise.com/repository/).

## Supported software environment

ArcticStack requires Ansible >= 2.9.13.

Supported OS:

  * Red Hat Enterprise Linux/CentOS 7
  * Red Hat Enterprise Linux/CentOS 8

**[OpenHPC](https://openhpc.community/downloads/)** scientific packages and
OpenHPC slurm job scheduler are compatible with the stack.

For Debian and Ubuntu users, take a look at [DebOps](https://debops.org).
