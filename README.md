[![pipeline status](https://gitlab.com/dudefellah/ansible-role-postgresql/badges/main/pipeline.svg)](https://gitlab.com/dudefellah/ansible-role-postgresql/-/commits/main)

PostgreSQL
=========

This Ansible role installs, configures and prepares a postgresql database on
a system. It largely borrows from enix.postgresql
(https://github.com/enix/ansible-postgresql) but is updated for more modern
Ansible releases and has a bunch of conveniences added. It's sufficiently
different that I ended up creating this new role rather than sending a PR
to the original role's author.

Requirements
------------

None.

Role Variables
--------------

Please see [defaults/main.yml](defaults/main.yml) for the list of settable
values. Each variable should be commented with details on their function.

Some values have distribution/version dependent defaults. Those can be found
in the appropriate files under [var/](var/), but any distribution-specific
value listed under this path can be overridden by providing a real value to
the associated variable listed in `defaults/main.yml`.

Dependencies
------------

None

Example Playbook
----------------

Basic installation is fairly straightforward.

    - hosts: pg_hosts
      roles:
         - { role: dudefellah.postgresql, postgres_version: 13 }

License
-------

GPLv3

Author Information
------------------

Dan - github.com/dudefellah
