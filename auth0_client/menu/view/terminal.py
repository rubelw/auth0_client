from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from datetime import datetime

from auth0_client.menu.commons.string import *
from auth0_client.menu.commons.io import print_safe
from auth0_client.menu.commons.types import *
from auth0_client.menu.entity import Menu, Command
from auth0_client.menu.exceptions import EncodingError, SettingError
from auth0_client.menu.view import i18n
import inspect
import re


DEBUG=0

DEFAULT_WINDOW_WIDTH = 78
DEFAULT_PAGE_SIZE = 32


class Terminal(object):
    def __init__(self, root_menu, host, user, executor, handler, width=None, page_size=None, _input=sys.stdin,
                 _output=sys.stdout, encoding=None, lang=None, timing=True, source_enabled=True):
        """
        :param root_menu: dict of root menu
        :param host: host name string
        :param user: user name string
        :param executor: Executor instance
        :param handler: auth0_client.menu.commons.terminal.TerminalHandler instance
        :param width:
        :param page_size:
        :param _input:
        :param _output:
        :param encoding:
        :param lang: language setting
        :param timing: bool: print running time after executing command if true
        :param source_enabled: bool: allow source printing if true
        :return:
        """

        if (DEBUG):
            print('terminal.py - __init__(self,root_menu,host,user,executor,handler, etc...)- caller:'+str(inspect.stack()[1][3]))

        # fields
        self.root_menu = root_menu
        self.host = host
        self.user = user
        self.executor = executor
        self.handler = handler
        self.width = DEFAULT_WINDOW_WIDTH if width is None else width
        self.page_size = DEFAULT_PAGE_SIZE if page_size is None else page_size
        self._input = _input
        self._output = _output
        self.encoding = encoding
        self.lang = lang
        self.i18n = self._find_i18n(lang)
        self.timing = timing
        self.source_enabled = source_enabled

        if self.width < 40:
            raise SettingError('width must be equal or greater than 40: width=%s' % self.width)
        if not 0 < self.page_size <= 32:
            raise SettingError('page_size must be positive and one digit: page_size=%s' % self.page_size)

    @staticmethod
    def _find_i18n(lang):
        if (DEBUG):
            print('terminal.py - _find_i18n(lang)- caller:'+str(inspect.stack()[1][3]))

        if not lang:
            return i18n.messages_en
        elif lang.lower().startswith('ja'):
            return i18n.messages_ja
        else:
            return i18n.messages_en

    def _num_pages(self, num_items):
        if (DEBUG):
            print('terminal.py - _num_pages(self,num_items)- caller:'+str(inspect.stack()[1][3]))

        return max(1, (num_items + self.page_size - 1) // self.page_size)

    #
    # Design parts
    #
    def thin_line(self):
        if (DEBUG):
            print('terminal.py - thin_line(self)- caller:'+str(inspect.stack()[1][3]))

        return '-' * self.width

    def thick_line(self):
        if (DEBUG):
            print('terminal.py - thick_line(self)- caller:'+str(inspect.stack()[1][3]))

        return '=' * self.width

    def header_line(self):
        if (DEBUG):
            print('terminal.py - header_line(self)- caller:'+str(inspect.stack()[1][3]))

        return edge_just(self.i18n.MSG_HOST % self.host, self.i18n.MSG_USER % self.user, self.width)

    @staticmethod
    def title_line(title):
        if (DEBUG):
            print('terminal.py - title_line(title)- caller:'+str(inspect.stack()[1][3]))

        return ' ' * 2 + title

    def menu_line(self):
        if (DEBUG):
            print('terminal.py - menu_line(self)- caller:'+str(inspect.stack()[1][3]))

        return '+'.rjust(7, '-').ljust(self.width, '-')

    def pager_line(self, offset, num_pages):
        if (DEBUG):
            print('terminal.py - pager_line(self,offset,num_pages)- caller:'+str(inspect.stack()[1][3]))

        left = '<= [P]' if 0 < offset else '      '
        right = '[N] =>' if offset + 1 < num_pages else '      '
        middle = ('Page %d / %d' % (offset + 1, num_pages)).center(self.width - len(left) - len(right))
        return left + middle + right

    #
    # Building output string
    #
    def _get_header(self, title):
        if (DEBUG):
            print('terminal.py - _get_header(self,title)- caller:'+str(inspect.stack()[1][3]))

        return [
            self.header_line(),
            self.thick_line(),
            self.title_line(title),
            self.thin_line(),
        ]

    def _get_footer(self, message):
        if (DEBUG):
            print('terminal.py - _get_footer(self,message)- caller:'+str(inspect.stack()[1][3]))

        return [
            self.thick_line(),
            message,
        ]

    def _get_description(self, item):
        if (DEBUG):
            print('terminal.py - _get_description(self,item)- caller:'+str(inspect.stack()[1][3]))

        return (self.i18n.MSG_SUB_MENU if isinstance(item, Menu) else '%s') % item.title

    def _get_breadcrumb(self, titles):
        if (DEBUG):
            print('terminal.py - _get_breadcrumb(self,titles)- caller:'+str(inspect.stack()[1][3]))

        s = ' > '.join(titles)
        n = unicode_width(s)
        limit = self.width - 5
        return ('~' if limit < n else '') + unicode_right(s, limit)

    def get_page(self, titles, page_items, offset, num_pages):
        """Make menu page string."""

        if (DEBUG):
            print('terminal.py - get_page(self,titles,page_items,offset,num_pages)- caller:'+str(inspect.stack()[1][3]))

        assert len(page_items) <= self.page_size, 'Number of page items must less or equal than page size.'

        title = self._get_breadcrumb(titles)

        pager_lines = [] if num_pages <= 1 else [
            self.pager_line(offset, num_pages),
            self.thin_line(),
        ]

        item_lines = [self.i18n.MSG_ITEM % (i + 1, self._get_description(item)) for i, item in enumerate(page_items)]

        quit_lines = [
            self.menu_line(),
            self.i18n.MSG_ITEM % (
                0, self.i18n.MSG_QUIT if len(titles) == 1 else self.i18n.MSG_RETURN % titles[-2]),
        ]

        message = self.i18n.MSG_INPUT_NUM % (0, len(page_items))
        return '\n'.join(self._get_header(title) + pager_lines + item_lines + quit_lines + self._get_footer(message))

    def get_confirm(self, description):
        """
        Make confirmation page string

        :param description: description for the command to execute
        :return: string
        """
        if (DEBUG):
            print('terminalpy - get_confirm(self,description)- caller:'+str(inspect.stack()[1][3]))

        item_lines = [
            self.i18n.MSG_CONFIRM % description
        ]
        return '\n'.join(
            self._get_header(self.i18n.MSG_CONFIRM_TITLE) + item_lines +
            self._get_footer(self.i18n.MSG_CONFIRM_QUESTION))

    def get_duplicate(self, description):
        """
        Make duplicate check page string
        """
        if (DEBUG):
            print('terminal.py - get_duplicate(self,description)- caller:'+str(inspect.stack()[1][3]))

        item_lines = [
            self.i18n.MSG_DUPLICATE % description
        ]
        return '\n'.join(
            self._get_header(self.i18n.MSG_DUPLICATE_TITLE) + item_lines +
            self._get_footer(self.i18n.MSG_DUPLICATE_QUESTION)
        )

    def get_before_execute(self, description):
        if (DEBUG):
            print('terminal.py - get_before_execute(self,description)- caller:'+str(inspect.stack()[1][3]))

        return '\n'.join(self._get_header(self.i18n.MSG_RUN_TITLE % description) + [''])

    def get_after_execute(self, title, return_code, start_time, end_time):
        if (DEBUG):
            print('terminal.py - get_after_execute(self,title,return_code,start_time,end_time)- caller:'+str(inspect.stack()[1][3]))

        items = [('Return code', '%d' % return_code)]
        if self.timing:
            items = [
                (self.i18n.MSG_FINISH, title),
                ('Running time', '%s  (%s -> %s)' % (self._format_timedelta(end_time - start_time),
                                                     self._format_datetime(start_time),
                                                     self._format_datetime(end_time))),
            ] + items

        if sys.version_info[0] < 3:
            key_width = max(unicode_width(x[0]) for x in items)
            result_lines = [self.thin_line()] + ['%s: %s' % (unicode.ljust(k, key_width), v) for k, v in items]

        else:
            key_width = max(len(x[0]) for x in items)

            result_lines = [self.thin_line()] + ['%s: %s' % (str(k).ljust(int(key_width),' '), v) for k, v in items]

        return '\n'.join(result_lines + self._get_footer(self.i18n.MSG_INPUT_ANY))

    @staticmethod
    def _format_timedelta(tm):
        if (DEBUG):
            print('terminal.py - _format_timedelta(tm)- caller:'+str(inspect.stack()[1][3]))

        hour, second = divmod(tm.seconds, 60 * 60)
        minute, second = divmod(second, 60)

        if tm.days < 0:
            return ''
        elif tm.days > 0:
            return '%dd %dh %dm %ds' % (tm.days, hour, minute, second)
        elif hour > 0:
            return '%dh %dm %ds' % (hour, minute, second)
        elif minute > 0:
            return '%dm %ds' % (minute, second)
        elif second > 0:
            return '%ds' % second
        return '%dms' % (tm.microseconds // 1000)

    @staticmethod
    def _format_datetime(dt):
        if (DEBUG):
            print('terminal.py - _format_datetime(dt)- caller:'+str(inspect.stack()[1][3]))

        return dt.strftime('%Y-%m-%d %H:%M:%S')

    #
    # Wait for input
    #
    def wait_input_char(self):
        if (DEBUG):
            print('terminal.py - wait_input_char(self)- caller:'+str(inspect.stack()[1][3]))

        while True:

            ch = input()
            matchObj = re.match( r'(\d+)', ch, re.M|re.I)
            matchObj2 = re.match( r'(N|n|p|P)',ch, re.M|re.I)

            if matchObj:

                ch =  matchObj.group(1)

                if (DEBUG):
                    print('found input: '+str(ch))

                #ch = self.handler.getch()
                #if ch in ['\x03', '\x04']:
                # pressed C-c or C-d
                #@raise KeyboardInterrupt

                if (DEBUG):
                    print('input is:'+str(ch))
                return ch
            elif matchObj2:
                ch = matchObj2.group(1).lower()

                if (DEBUG):
                    print('found input: '+str(ch))

                return ch
            else:
                print('Please enter a number.')

    def wait_input_yes_no(self, default=False):
        if (DEBUG):
            print('terminal.py - wait_input_yes_no(self, default=False)- caller:'+str(inspect.stack()[1][3]))

        while True:
            ch = self.wait_input_char().lower()
            if ch == 'y':
                return True
            elif ch == 'n':
                return False
            elif ch == '\r' or not self.handler.getch_enabled:
                # default
                return default

    #
    # Output
    #
    def _print(self, unicode_text):
        if (DEBUG):
            print('terminal.py - _print(self, unicode_text)- caller:'+str(inspect.stack()[1][3]))

        assert is_unicode(unicode_text), 'Text must be unicode: %s' % unicode_text

        try:
            print_safe(unicode_text, self.encoding, output=self._output, errors='strict', newline='')
        except (LookupError, UnicodeError):
            raise EncodingError('Failed to print menu: lang=%s, encoding=%s' % (self.lang, self.encoding))

    def _draw(self, unicode_text):
        if (DEBUG):
            print('terminal.py - _draw(self,unicode_text)- caller:'+str(inspect.stack()[1][3]))

        self.handler.clear()
        self._print(unicode_text)

    #
    # Main loop
    #
    def wait_input_menu(self, menu_items, offset, num_pages):
        """
        :param menu_items: list of items
        :param offset: page offset
        :return: function(stack, offset => stack, offset)
        """
        if (DEBUG):
            print('################### Main Loop #####################')
            print('terminal.py - wait_input_menu(self, menu_items, offset, num_pages)- caller:'+str(inspect.stack()[1][3]))


        num_items = len(menu_items)

        while True:

            ch = self.wait_input_char().lower()

            if ch == '0':
                return lambda s, o: (s[:-1], 0)
            elif ch.isdigit():
                index = offset * self.page_size + int(ch) - 1
                if index < num_items:
                    item = menu_items[index]

                    # check if it is a sub menu
                    if isinstance(item, Menu):
                        return lambda s, o: (s + [item], 0)

                    def f(s, o):  # side effect only
                        self.execute_command(item)
                        return s, o

                    return f
            elif ch == 'n' and offset + 1 < num_pages:
                return lambda s, o: (s, o + 1)
            elif ch == 'p' and 0 < offset:
                return lambda s, o: (s, o - 1)
            elif ch == 's' and self.source_enabled:
                def f(s, o):  # side effect only
                    self.print_source()
                    return s, o
                return f

            # if getch is disabled, redraw screen
            if not self.handler.getch_enabled:
                return lambda s, o: (s, o)

    @types(command=Command)
    def execute_command(self, command):
        """
        Confirm with prompt before executing command.

        :param command: Command:
        :return: None
        """
        if (DEBUG):
            print('terminal.py - execute_command(self, command)- caller:'+str(inspect.stack()[1][3]))

        # confirmation
        #self._draw(self.get_confirm(command.title))
        #if not self.wait_input_yes_no():
        #    return

        # duplicate check
        #if self.executor.is_running(command):
        #    self._draw(self.get_duplicate(command.title))
        #    if not self.wait_input_yes_no():
        #        return

        # run command
        start_time = datetime.now()
        self._draw(self.get_before_execute(command.title))
        return_code = self.executor.execute(command)
        end_time = datetime.now()
        if return_code == 130:
            # maybe interrupted
            self._print('\n')

        self._print(self.get_after_execute(command.title, return_code, start_time, end_time))
        self.wait_carriage_return()  # wait for any input

    #
    # Wait for input
    #
    def wait_carriage_return(self):
        if (DEBUG):
            print('terminal.py - wait_carriage_return(self)- caller:'+str(inspect.stack()[1][3]))

        ch = self.handler.getch()


        if (DEBUG):
            print('input is:'+str(ch))
        return ch


    def print_source(self):
        """Print source of the root menu."""
        if (DEBUG):
            print('terminal.py - print_source(self)- caller:'+str(inspect.stack()[1][3]))

        self._draw('\n'.join(self._get_header(self.i18n.MSG_SOURCE_TITLE)))
        self._print('\n%s\n' % self.root_menu.formatted())
        self._print('\n'.join(self._get_footer(self.i18n.MSG_INPUT_ANY)))
        self.wait_input_char()

    def loop(self):

        if (DEBUG):
            print('###################### Looping #############################')
            print('terminal.py - loop(self)- caller:'+str(inspect.stack()[1][3]))

        stack = [self.root_menu]
        offset = 0  # current page index

        while stack:
            titles = [menu.title for menu in stack]
            items = stack[-1].items
            num_pages = self._num_pages(len(items))

            # apply offset
            page_items = items[self.page_size * offset:self.page_size * (offset + 1)]

            self._draw(self.get_page(titles, page_items, offset, num_pages))

            f = self.wait_input_menu(items, offset, num_pages)
            stack, offset = f(stack, offset)

        self.handler.clear()
