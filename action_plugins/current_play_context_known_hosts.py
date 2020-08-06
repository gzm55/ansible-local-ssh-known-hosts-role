from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        ctx = self._play_context

        # connection common
        result['connection'] = ctx.connection
        result['remote_addr'] = ctx.remote_addr
        result['port'] = ctx.port
        result['ssh_executable'] = ctx.ssh_executable

        result['changed'] = False
        return result
