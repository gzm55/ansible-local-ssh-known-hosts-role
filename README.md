[![Build Status](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role.svg?branch=master)](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role)

local_ssh_known_hosts (1.0.1)
=================================

A Role for accepting ssh fingerprints automatically for the first time.

Requirements
------------

ansible>=2.7
jinja2>=2.7

For `ansible<2.7`, use version 0.0.3.

Role Variables
--------------

None.

Dependencies
------------

- `gzm55.require_implicity_localhost`
- `gzm55.require_disabe_become`
- `gzm55.require_local_command`
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
