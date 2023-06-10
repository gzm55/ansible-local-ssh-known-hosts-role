[![Build Status](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role.svg?branch=master)](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role)

local_ssh_known_hosts (2.0.0)
=================================

A Role for accepting ssh fingerprints automatically for the first time.

Requirements
------------

ansible-core>=2.12
jinja2>=2.7

Test with matrix:
- python 3.8 + ansible-core 2.13
- python 3.10 + ansible-core 2.14

For `ansible<2.7`, use version 0.0.3.
For `ansible<2.12`, use version 1.0.2.

Role Variables
--------------

None.

Dependencies
------------

- `gzm55.require_implicity_localhost`
- `gzm55.require_disabe_become`
- `gzm55.local_id_plugin`

Example Playbook
----------------

    - hosts: all
      gather_facts: False
      roles:
      - gzm55.local_ssh_known_hosts

License
-------

BSD
