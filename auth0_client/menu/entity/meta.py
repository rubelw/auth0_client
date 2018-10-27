from __future__ import division, print_function, absolute_import, unicode_literals

import copy
from auth0_client.menu.commons.case_class import CaseClass
from auth0_client.menu.commons.types import *
from auth0_client.menu.commons.string import to_unicode
import inspect

DEBUG=1

class Meta(CaseClass):
    """
    Meta settings for running commands
    """

    @types(work_dir=Option(Unicode), env=Option(DictOf(Unicode, Unicode)), lock=bool)
    def __init__(self, work_dir=None, env=None, lock=False):
        """
        :param work_dir:
        :param env:
        :param lock:
        :return:
        """
        if (DEBUG):
            print('entity.meta.py - Meta - __init__(self,work_dir,env,lock)- caller:'+str(inspect.stack()[1][3]))

        env = env or {}
        CaseClass.__init__(self, ('work_dir', work_dir), ('env', env), ('lock', lock))

    @types(data=dict)
    def updated(self, data, encoding):
        """
        Load configuration and return updated instance.
        :param data: dict:
        :return: Meta:
        """
        if (DEBUG):
            print('entity.meta.py - Meta - updated(self,data,encoding)- caller:'+str(inspect.stack()[1][3]))

        functions = {
            'work_dir': Meta._load_work_dir,
            'env': Meta._load_env,
            'lock': Meta._load_lock,
        }

        ret = self.copy()
        for k, v in data.items():
            ret = functions.get(k, self.__unknown_field(k))(ret, v, encoding)
        return ret

    @types(data=String, encoding=String)
    def _load_work_dir(self, data, encoding):
        """Overwrite working directory"""
        if (DEBUG):
            print('entity.meta.py - Meta -  _load_work_dir(self,data,encoding)- caller:'+str(inspect.stack()[1][3]))

        self.work_dir = to_unicode(data, encoding)
        return self

    @types(data=DictOf(String, String), encoding=String)
    def _load_env(self, data, encoding):
        """Merge environment variables"""
        if (DEBUG):
            print('entity.meta.py - _load_env(self,data,encoding)- caller:'+str(inspect.stack()[1][3]))

        d = copy.copy(self.env)
        d.update([(to_unicode(k, encoding), to_unicode(v, encoding)) for k, v in data.items()])
        self.env = d
        return self

    @types(data=bool, encoding=String)
    def _load_lock(self, data, encoding):
        """Overwrite lock setting"""
        if (DEBUG):
            print('entity.meta.py - Meta - _load_lock(self,data,encoding)- caller:'+str(inspect.stack()[1][3]))

        self.lock = data
        return self

    @staticmethod
    def __unknown_field(key):
        if (DEBUG):
            print('entity.meta.py - Meta - _unknown_field(key)- caller:'+str(inspect.stack()[1][3]))

        def f(x, y, z):
            raise ValueError('Unknown field: %s' % key)

        return f
