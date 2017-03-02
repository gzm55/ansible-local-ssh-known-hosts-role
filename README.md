[![Build Status](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role.svg?branch=master)](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role)

local_ssh_known_hosts
=========

A Role for accepting ssh fingerprints automatically for the first time.

Requirements
------------

ansible>=2.0
jinja2>=2.7

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
