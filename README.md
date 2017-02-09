[![Build Status](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role.svg?branch=master)](https://travis-ci.org/gzm55/ansible-local-ssh-known-hosts-role)

local_ssh_known_hosts
=========

A Role for accepting ssh fingerprints automatically for the first time.

Requirements
------------

ansible>=2.0
jinja2>=2.8

Role Variables
--------------

None.

Dependencies
------------

- `gzm55.local_ansible_config`
- `gzm55.require_local_command`

Example Playbook
----------------

    - hosts: all
      gather_facts: False
      roles:
      - gzm55.local_ssh_known_hosts

License
-------

BSD
