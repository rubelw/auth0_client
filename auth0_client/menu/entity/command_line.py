from __future__ import division, print_function, absolute_import, unicode_literals

import os
import hashlib
from auth0_client.menu.commons.case_class import CaseClass
from auth0_client.menu.commons.collection import get_single_item
from auth0_client.menu.commons.functional import oget
from auth0_client.menu.commons.types import *
from auth0_client.menu.commons.string import to_unicode, is_strlike, to_bytes
from auth0_client.menu.entity import Meta
import inspect

DEBUG=1


class CommandLine(CaseClass):
    @types(cmd=Unicode, meta=Meta, encoding=String)
    def __init__(self, cmd, meta, encoding='utf-8'):
        """
        :param cmd: command line string
        :param meta:
        :param encoding: encoding for command line string
        :return:
        """
        if (DEBUG):
            print('entity.command_line.py - CommandLine - __init__(self,cmd,meta,encoding)- caller:'+str(inspect.stack()[1][3]))

        CaseClass.__init__(self, ('cmd', cmd), ('meta', meta), ('encoding', encoding))

    @staticmethod
    def parse(data, meta, encoding='utf-8'):
        """
        Parse one command line.
        :param data: string or dict:
        :param meta: Meta: meta configuration inherited from the parent menu
        :param encoding: string:
        :return: CommandLine:
        """
        if (DEBUG):
            print('entity.command_line.py  CommandLine- parse()- caller:'+str(inspect.stack()[1][3]))

        assert isinstance(meta, Meta)

        def f(s):
            return to_unicode(s, encoding)

        if is_strlike(data):
            return CommandLine(f(data), meta, encoding)
        elif isinstance(data, dict):
            cmd, params = get_single_item(data)
            assert is_strlike(cmd), 'cmd must be string, not %s.' % type(cmd).__name__
            new_meta = meta.updated(params, encoding)
            return CommandLine(to_unicode(cmd, encoding), new_meta, encoding)
        else:
            raise ValueError('CommandLine must be string or dict, not %s.' % type(data).__name__)

    @types(Unicode)
    def formatted(self):
        if (DEBUG):
            print('entity.command_line.py - CommandLine - formatted()- caller:'+str(inspect.stack()[1][3]))

        buf = [
            '- cmd: %s' % self.cmd,
            '  cwd: %s' % oget(self.meta.work_dir, os.path.abspath(os.path.curdir)),
        ]
        if self.meta.env:
            buf.append('  env: {%s}' % ', '.join('%s: %s' % (k, v) for k, v in sorted(self.meta.env.items())))
        if self.meta.lock:
            buf.append('  lock: True')
        return '\n'.join(buf)

    @types(String)
    def to_hash_string(self):
        if (DEBUG):
            print('entity.command_line.py - CommandLine - to_hash_string()- caller:'+str(inspect.stack()[1][3]))

        # ignore work directory
        data = b''.join(to_bytes(s) for s in [self.cmd, sorted(self.meta.env.items())])

        return hashlib.md5(data).hexdigest()
