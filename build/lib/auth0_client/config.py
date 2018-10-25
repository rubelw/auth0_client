"""
Configuration and related utilities for CLI-specific functionality.

This is kept separate from auth0-client main config
"""


CLI_COLORS = ['white', 'black', 'red', 'yellow', 'green', 'cyan', 'blue', 'magenta', None]
""" Colors compatible with :py:func:`click.style` """

CLI_STATUS =  'green'
CLI_EXAMPLE =  'yellow'
CLI_RESOURCE =  'white'
CLI_SUCCESS = 'cyan'
CLI_WARNING =  'red'
CLI_ERROR =  'red'
CLI_VERSION =  'blue'
HELP_COLORS = {
    'help_headers_color': CLI_STATUS,
    'help_options_color': CLI_EXAMPLE,
}

