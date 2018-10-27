from __future__ import division, print_function, absolute_import, unicode_literals

import os
import sys
import locale
from auth0_client.menu.commons.case_class import CaseClass
from auth0_client.menu.commons.functional import omap, oget
from auth0_client.menu.commons.string import to_unicode

from auth0_client.menu.setting import arg_parser
from auth0_client.menu.setting.loader import Loader
from auth0_client.menu.entity import Menu, Meta
from auth0_client.menu.exceptions import SettingError, ConfigError
import inspect


DEBUG=0

DEFAULT_CONFIG_NAME = ""

DATAFILES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))+'/datafiles'

DEFAULT_CONFIG_NAME= str(DATAFILES_DIR)+'/auth-menu.yml'

EVAL_CACHE_DIR = os.path.join(os.path.expanduser('~'), '.auth-menu', 'eval')
COMMAND_PID_DIR = os.path.join(os.path.expanduser('~'), '.auth-menu', 'pid')


class Setting(CaseClass):
    """
    Manages all settings.
    """

    def __init__(self, config_path=None, work_dir=None, root_menu=None, encoding=None, lang=None, width=None,
                 clear_cache=False, cache_dir=EVAL_CACHE_DIR, pid_dir=COMMAND_PID_DIR,
                 stdin=None, stdout=None, stderr=None, getch_enabled=True, source_enabled=True):

        if (DEBUG):
            print('settings.settings.py - __init__(self,etc...)- caller:'+str(inspect.stack()[1][3]))

        is_url = Loader.is_url(config_path)
        #work_dir = omap(lambda s: to_unicode(s, encoding), self._search_work_dir(work_dir, config_path, is_url))
        work_dir = ""


        work_dir = os.path.join(os.path.expanduser('~'), '.auth-menu', 'tmp')


        CaseClass.__init__(self,
                           ('config_path', config_path),
                           ('work_dir', work_dir),
                           ('root_menu', oget(root_menu, {})),
                           ('encoding', encoding),
                           ('lang', self._find_lang(lang)),
                           ('width', width),
                           ('clear_cache', clear_cache),
                           ('cache_dir', cache_dir),
                           ('pid_dir', pid_dir),
                           ('stdin', oget(stdin, sys.stdin)),
                           ('stdout', oget(stdout, sys.stdout)),
                           ('stderr', oget(stderr, sys.stderr)),
                           ('getch_enabled', getch_enabled),
                           ('source_enabled', source_enabled)
                           )

    @staticmethod
    def _find_lang(lang):
        if (DEBUG):
            print('settings.settings.py - _find_lang()- caller:'+str(inspect.stack()[1][3]))

        if not lang:
            # environment LANG is the first priority
            lang = os.environ.get('LANG')
        if not lang:
            lang = locale.getdefaultlocale()[0]

        if (DEBUG):
            print("\t"+'returning: '+str(lang))

        return lang

    @staticmethod
    def _search_work_dir(work_dir, config_path, is_url):

        if (DEBUG):
            print('settings.settings.py- _search_work_dir()- caller:'+str(inspect.stack()[1][3]))

        if work_dir is None:
            if config_path is not None:
                if not is_url:
                    return os.path.dirname(config_path)

        if (DEBUG):
            print("\t"+'returning :'+str(work_dir))

        return work_dir

    def resolve_encoding(self, terminal_handler):

        if (DEBUG):
            print('settings.settings.py - resolve_encoding(self,terminal_handler)- caller:'+str(inspect.stack()[1][3]))

        if not self.encoding:
            return self.copy(encoding=terminal_handler.encoding)
        return self

    def parse_args(self, argv):

        if (DEBUG):
            print('settings.settings.py - parse_args(self,argv)- caller:'+str(inspect.stack()[1][3]))

        option, args = arg_parser.parser.parse_args(argv[1:])
        path = None

        if not args:
            pass
        elif len(args) == 1:
            path = args[0]
            if not Loader.is_url(path):
                path = os.path.abspath(path)
        else:
            arg_parser.parser.print_help()
            arg_parser.parser.exit(2)

        return self.copy(config_path=path, work_dir=option.work_dir, encoding=option.encoding, lang=option.lang,
                         width=option.width, clear_cache=option.clear_cache, getch_enabled=option.getch_enabled)

    def lookup_config(self):

        if (DEBUG):
            print('settings.settings.py - lookup_config(self)- caller:'+str(inspect.stack()[1][3]))

        if self.config_path is None:
            d = os.path.abspath(self.work_dir) if self.work_dir else os.getcwd()

            while True:
                path = os.path.join(d, DEFAULT_CONFIG_NAME)
                if os.path.exists(path):
                    return self.copy(config_path=path)
                nd = os.path.dirname(d)
                if d == nd:
                    break
                d = nd
        return self

    def load_config(self):

        if (DEBUG):
            print('settings.settings.py - load_config(self)- caller:'+str(inspect.stack()[1][3]))

        """
        Load the configuration file or url.

        If it contains 'include' sections, load them recursively.
        :return: updated Setting instance
        """
        if self.config_path is None:
            raise SettingError('Not found configuration file.')

        loader = Loader(self.work_dir, self.cache_dir, self.encoding, self.stdout, self.clear_cache)
        data = loader.load(False, self.config_path)
        try:
            root_menu = Menu.parse(data, Meta(self.work_dir), loader, self.encoding, 0)
        except (AssertionError, ValueError, TypeError) as e:
            raise ConfigError(self.config_path, e)

        print('########### Done Loading Config File ################')
        return self.copy(root_menu=root_menu)
