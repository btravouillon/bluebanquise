# Contributing

:construction_worker: Many thanks for considering contributing to
**ArcticStack**. :construction_worker:

## Reporting bugs :beetle:

If you encounter any bug, please file an issue with the following details:

 - How did you end up to this bug?
 - What were you expecting as a normal result?
 - Full trace of the output
 - Your operating system distribution and version
 - Your Ansible version

If the bug is related to PXE or OS deployment:

 - Is the system EFI or legacy/bios?
 - What is the native ROM of the system, PXE or iPXE?
 - Do you use PXE boot or USB/CD-ROM boot?
 - What is the hardware used?
 - If possible, a photo/screenshot of the screen when it fails.

We may ask you more questions and data to reproduce the issue. **Do not provide
security related data (ssh key, passwords, etc) in your reports.**

## Asking for new features / enhancements :bulb:

We would be happy to enhance the stack with new ideas and features.

However, please keep in mind we are maintaining the project on our spare time,
as a **best effort** :family:. We will do our best to at least acknowledge we
got your query.

Also, if we consider a feature request does not comply with the objectives of
the stack, we may reject the feature (with an explanation). Don't take offense.

## Pull Requests :arrow_heading_down:

To submit any contribution, create a Pull Request (PR).

We will do our best to review and test your contribution as soon as possible,
before merging it. We may iterate with you to converge before merging to the
devel branch.

### Backports

All PRs must be merged to the **devel** branch first. Once merged, you can create
a new PR to backport the change to a previous stable branch.

For backports, we use a workflow similar to the [Ansible Development
Cycle](https://docs.ansible.com/ansible/latest/community/development_process.html#backporting-merged-prs-in-ansible-base).

We do **not** backport features.

Whenever possible, please cherry-pick the commit using the `-x` flag to
indicate which commit this change was cherry-picked from.

```bash
git fetch upstream
git checkout -b backport/1.4/<pr_number_from_master> upstream/stable-1.4
git cherry-pick -x <commit_from_master>
git push origin backport/1.4/<pr_number_from_master>
```

Submit the PR for `backport/1.4/<pr_number_from_master>` against the
`stable-1.4` branch.

## Development guidelines :octopus:

### Documenting, comments

1. When possible, try to add balanced comments, considering you are teaching to
someone. Feel free to add URL to references or tutorials, etc.

2. **Always document**, either in the main documentation or in the readme files
of the roles. Documentation is written in reStructuredText for use with the
Sphinx documentation generator.

### Scripting

1. Scripts should be written in *Python 3.6+* or *Bash*. Comments and verbosity
should be considered.

2. Tools, scripts and wrappers are written to simplify system usage (Shell
commands, Ansible, Linux tools, etc.). However, when possible, manual way
should always be documented alongside with the automated way, to allow easy
debug and simple understanding of the scripts.

### Variables

1. General variables, i.e. not related to an equipment_profile, can be defined
in group_vars/all/general_settings/, in dedicated files. Whenever possible,
variables should be optional. In any case, variables must be documented in the
readme of the role (and, if needed, in the example inventories).

2. All variables related to an equipment_profile should be in
group_vars/all/equipment_all/ (global) or in group_vars/equipment_X/ with X the
equipment profile name (dedicated). These variables must be prefixed by
**ep_**.

### Conventions

1. Numbering  starts at **1**, since a cluster stack is related to existing
physical elements (Networks start at 1, icebergs at 1, etc.).

2. YAML files extension is *.yml* (not *.yaml*).

3. Avoid tabulations, prefer double space for indentation.

4. If you are working on Microsoft Windows, please ensure you do not submit
CRLF (seen sometime as ^M at the end of your lines). See
[Customizing-Git-Git-Configuration](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_code_core_autocrlf_code).

5. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
and commits adheres to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## License

**ArcticStack** is licensed under the MIT license. This choice is based on the
wish to allow everyone to use and contribute to the project.

If you do not wish to use the MIT license but still want to contribute, please
contact us.
