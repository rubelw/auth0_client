from __future__ import division, print_function, absolute_import, unicode_literals

from optparse import OptionParser
import inspect

DEBUG=0

VERSION = 'auth-menu %s' % __import__('auth0_client').__version__

USAGE = """%prog [options...] [<config_path> | <config_url>]"""


def __get_parser():
    p = OptionParser(version=VERSION, usage=USAGE)

    if (DEBUG):
        print('settings.arg_parser.py - __get_parser()- caller:'+str(inspect.stack()[1][3]))

    p.add_option(
        '--encode', dest='encoding', default=None, type='string', metavar='ENCODING',
        help='set output encoding to ENCODING'
    )

    p.add_option(
        '--lang', dest='lang', default=None, type='string', metavar='LANG',
        help='set language to LANG (in RFC 1766 format)'
    )

    p.add_option(
        '--width', dest='width', default=None, type='int', metavar='WIDTH',
        help='set window width to WIDTH'
    )

    p.add_option(
        '-d', '--work-dir', dest='work_dir', default=None, type='string', metavar='DIR',
        help='set working directory to DIR'
    )

    p.add_option(
        '--clear-cache', dest='clear_cache', action='store_true', default=False,
        help='clear old cache when evaluating "eval" section (default: False)'
    )

    p.add_option(
        '--no-getch', dest='getch_enabled', action='store_false', default=True,
        help='disable real-time key input (without pressing ENTER key) (default: enabled)'
    )
    return p


parser = __get_parser()
