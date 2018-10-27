from __future__ import division, print_function, absolute_import, unicode_literals

from abc import ABCMeta, abstractmethod
import six
import inspect

DEBUG=1

@six.add_metaclass(ABCMeta)
class Executor(object):
    """abstract executor class"""

    @abstractmethod
    def execute(self, command):
        if (DEBUG):
            print('controller.executor.py - execute(self,command) - caller:'+str(inspect.stack()[1][3]))

        """abstract method"""

    def is_running(self, command):
        if (DEBUG):
            print('controller.executor.py - is_running(self,command) - caller:'+str(inspect.stack()[1][3]))

        """abstract method"""
