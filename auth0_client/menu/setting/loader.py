from __future__ import division, print_function, absolute_import, unicode_literals

import os
import sys
import time
import re
import yaml
import hashlib
from six.moves.urllib.request import urlopen
from jinja2 import Environment
from auth0_client.menu.commons.command import capture_command
from auth0_client.menu.commons.string import *
from auth0_client.menu.commons.io import print_safe
from auth0_client.menu.commons.types import *
from auth0_client.menu.exceptions import ConfigError, EncodingError
import inspect

DEBUG=0

URL_PATTERN = re.compile(r'^http[s]?://')


class Loader(object):
    def __init__(self, work_dir, cache_dir, encoding='utf-8', stdout=sys.stdout, clear_cache=False):
        if (DEBUG):
            print('settings.loader.py - __init__(self,work_dir, etc...)- caller:'+str(inspect.stack()[1][3]))

        self.work_dir = work_dir
        self.cache_dir = cache_dir
        self.encoding = encoding
        self.stdout = stdout
        self.clear_cache = clear_cache
        self.cache = {}

    @staticmethod
    def is_url(path):
        if (DEBUG):
            print('settings.loader.py - is_url(path)- caller:'+str(inspect.stack()[1][3]))

        return path is not None and bool(URL_PATTERN.match(path))

    @types(is_command=bool, path_or_url_or_cmdline=String, eval_expire=Option(int))
    def load(self, is_command, path_or_url_or_cmdline, eval_expire=None):
        """
        Load data from one file, url or command line, then store to a dict.

        :param is_command: True if using command line output
        :param path_or_url_or_cmdline:
        :param eval_expire: seconds to read
        :return: dict representation of data
        """
        if (DEBUG):
            print('settings.loader.py - load(self,is_command,path_or_url_or_cmdline=String, eval_expire=Option(int))- caller:'+str(inspect.stack()[1][3]))
            print("\t"+'is_command: '+str(is_command))

            """
            This is the yml file
            """
            print("\t"+'path_or_url_or_cmdline:'+str(path_or_url_or_cmdline))


        assert path_or_url_or_cmdline

        # normalize file path
        is_url = self.is_url(path_or_url_or_cmdline)
        if not is_command and not is_url:
            if self.work_dir is not None and not os.path.isabs(path_or_url_or_cmdline):
                path_or_url_or_cmdline = os.path.join(self.work_dir, path_or_url_or_cmdline)

        # if already loaded, use cache data
        c = self.cache.get((is_command, path_or_url_or_cmdline))
        if c is not None:
            if (DEBUG):
                print("\t"+'yml file already cached')
            return c

        try:
            if is_command:
                # execute command
                if (DEBUG):
                    print("\t"+'is_command')

                if eval_expire is None:
                    data = self._eval_command(path_or_url_or_cmdline)
                else:
                    # if eval_expire is defined, check the cache on disk
                    data = self._eval_command_with_cache(path_or_url_or_cmdline, eval_expire)
            elif self.is_url(path_or_url_or_cmdline):
                # read from URL
                if (DEBUG):
                    print("\t"+'read from URL')

                print_safe('Reading from URL: %s' % path_or_url_or_cmdline, self.encoding, output=self.stdout)
                data = urlopen(path_or_url_or_cmdline).read()
            else:
                # read from file as bytes
                if (DEBUG):
                    print("\t"+'read from file as bytes')

                print_safe('Reading file: %s' % path_or_url_or_cmdline, self.encoding, output=self.stdout)
                with open(path_or_url_or_cmdline, 'rb') as f:
                    data = f.read()

            # decode string with fallback
            data_str = unicode_decode(data, [self.encoding, 'utf-8'])

            # apply jinja2 template rendering
            try:
                data_str = Environment().from_string(data_str).render()
            finally:
                pass

            # load as YAML string
            menu = yaml.load(data_str)

            if (DEBUG):
                print('menu is:'+str(menu))

            # update cache data (Note: cache property is mutable!)
            self.cache[(is_command, path_or_url_or_cmdline)] = menu
        except IOError:
            raise ConfigError(path_or_url_or_cmdline, 'Failed to open.')
        except UnicodeDecodeError:
            raise EncodingError('Failed to decode with %s: %s' % (self.encoding, path_or_url_or_cmdline))
        except yaml.YAMLError as e:
            raise ConfigError(path_or_url_or_cmdline, 'YAML format error: %s' % to_unicode(str(e)))
        return menu

    def _eval_command(self, cmdline):
        """
        :param cmdline:
        :return: encoded binary
        """

        # return code and stderr are ignored
        print_safe('Executing: %s' % cmdline, self.encoding, output=self.stdout)
        return capture_command(cmdline, shell=True, cwd=self.work_dir, cmd_encoding=self.encoding)[1]

    @types(cmdline=String, expire=int)
    def _eval_command_with_cache(self, cmdline, expire):
        path = self._eval_cache_path(cmdline)

        if (DEBUG):
            print('settings.loader.py - _eval_command_with_cache(self,cmdline,expire)- caller:'+str(inspect.stack()[1][3]))

        # read cache
        is_readable = not self.clear_cache and os.path.exists(path) and (time.time() - os.path.getmtime(path)) < expire
        if is_readable:
            print_safe('Reading eval cache: %s' % path, self.encoding, output=self.stdout)
            with open(path, 'rb') as f:
                return f.read()

        # execute command
        data = self._eval_command(cmdline)

        # write cache
        print_safe('Writing eval cache: %s' % path, self.encoding, output=self.stdout)

        # make parent directory
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        with open(self._eval_cache_path(cmdline), 'wb') as f:
            f.write(data)
        return data

    def _eval_cache_path(self, cmdline):
        if (DEBUG):
            print('settings.loader.py - _eval_cache_path(self,cmdline)- caller:'+str(inspect.stack()[1][3]))

        h = hashlib.md5(to_bytes(cmdline, self.encoding)).hexdigest()
        return os.path.join(self.cache_dir, h[:2], h[2:])
