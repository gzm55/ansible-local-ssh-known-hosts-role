Role Name
=========

A Role for accepting ssh fingerprints automatically for the first time.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all
      gather_facts: False
      roles:
      - gzm55.local_ssh_known_hosts

License
-------

BSD
