# coding: utf-8
""" CLI output formatting & related utilities """
from __future__ import unicode_literals
from future.types.newstr import newstr

from collections import Mapping, Sequence
import os
import re

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from reprint import output
from six import string_types, text_type
from tabulate import tabulate
from configparser import RawConfigParser
from collections import OrderedDict



from auth0_client.config import CLI_EXAMPLE, CLI_STATUS, CLI_SUCCESS, HELP_COLORS

FORMAT_CHARS = '┌┬┐└┴┘├─┼┤│╒╤╕╘╧╛╞╪╡╔╦╗╚╩╝╠═╬╣║┏┳┓┗┻┛┣━╋┫┃❰❱•◉'
TO_LOWER = {'token_normalize_func': str.lower}


def get_config_dict(ini_file, debug):

    ini_data = read_config_info(ini_file)


    config_dict = {}

    if debug:
        print('ini file is: ' + str(ini_data))
        config_dict['debug'] = debug

    if ini_data['parameters']['domain']:
        config_dict['domain'] = ini_data['parameters']['domain']
    if ini_data['parameters']['id']:
        config_dict['client_id'] = ini_data['parameters']['id']
    if ini_data['parameters']['secret']:
        config_dict['client_secret'] = ini_data['parameters']['secret']

    return config_dict


def read_config_info(ini_file):
    """
    Read the INI file
    Args:
        ini_file - path to the file
    Returns:
        A dictionary of stuff from the INI file
    Exits:
        1 - if problems are encountered
    """
    try:
        config = RawConfigParser()
        config.optionxform = lambda option: option
        config.read(ini_file)
        the_stuff = {}
        for section in config.sections():
            the_stuff[str(section)] = {}
            for option in config.options(section):
                the_stuff[str(section)][str(option)] = str(config.get(section, option.replace('\n', '')))

        return the_stuff
    except Exception as wtf:
        logging.error('Exception caught in read_config_info(): {}'.format(wtf))
        traceback.print_exc(file=sys.stdout)
        return sys.exit(1)




def highlight(text, highlight_strs, color):
    """
    Highlight specific strings or characters in text.
    See :py:func:`click.style` for supported colors.

    Args:
        text (str): Text containing strings to highlight
        highlight_strs (list): Specific strings to be highlighted
        color (str): Color to highlight with

    Returns:
        str: The provided ``text``, with added color (if ``highlight_strs`` were found)
    """
    for s in sorted(highlight_strs or [], key=len, reverse=True):
        # Add color, except for substrings that have already been colored (preceded by '[##m')
        text = re.sub(r'(?<!\[\d\dm)' + s, click.style(s, fg=color), text)
    return text


def sconfirm(confirm_msg, color=CLI_STATUS, **confirm_args):
    """
    py:func:`click.confirm`, but with colored confirmation text.
    See :py:func:`click.style` for supported colors.

    Args:
        confirm_msg (str): Confirmation message
        color (str): Color for confirmation message
        \\*\\*confirm_args (dict): Additional keyword arguments to :py:func:`click.confirm`

    Returns:
        bool: User response
    """
    return click.confirm(click.style(confirm_msg, fg=color), **confirm_args)


def sprompt(prompt_msg, color=CLI_STATUS, **prompt_args):
    """
    :py:func:`click.prompt`, but with colored prompt text.
    See :py:func:`click.style` for supported colors.

    Args:
        prompt_msg (str): Prompt message
        color (str): Color for prompt message
        \\*\\*prompt_args (dict): Additional keyword arguments to :py:func:`click.prompt`

    Returns:
        str: User input
    """
    return click.prompt(click.style(prompt_msg, fg=color), **prompt_args)


def shmecho(strs, colors):
    """
    Like :py:func:`click.secho`, but styles multiple strings with different colors.
    See :py:func:`click.style` for supported colors.

    Args:
        strs (list): List of strs to style
        colors (list): List of colors to apply
    """
    click.echo(''.join([click.style(text_type(s), fg=color or 'reset')
                        for s, color in zip(strs, colors)]))


def format_dict(d, highlight_strs=None, depth=0):
    """
    Format a dict with colored key-value pairs

    Args:
        d (dict): A dictionary (or other mapping) to format
        highlight_strs (list): Additional specific strings to be highlighted
        depth (int): Recursive depth of dictionary

    Returns:
        str: Dictionary as a formatted block of text
    """
    def format_value(v):
        if isinstance(v, Mapping):
            return '\n' + format_dict(v, highlight_strs=highlight_strs, depth=depth + 1)
        elif isinstance(v, Sequence) and not isinstance(v, string_types):
            return '\n' + indent(('\n'.join(v)), 4)
        else:
            return text_type(v)

    formatted = '\n'.join(['{}: {}'.format(click.style(k, fg='green'), format_value(v))
                           for k, v in d.items() if v])
    formatted = indent(formatted, 4 * depth)
    return highlight(formatted, highlight_strs, CLI_EXAMPLE)


def format_diagram(diagram, highlight_strs=None):
    """
    Format a tree, table, list, or other pre-stringified data structure with colored unicode
    formatting and optional additional coloring

    Args:
        diagram (str): Stringified diagram, as a block of text
        highlight_strs (list): Additional specific strings to be highlighted
    """
    # Colorize table formatting characters (and any optional highlight strings)
    diagram = highlight(diagram, FORMAT_CHARS, CLI_STATUS)
    diagram = highlight(diagram, highlight_strs, CLI_EXAMPLE)
    return diagram


def print_diagram(diagram, highlight_strs=None, **echo_args):
    """
    Print a formatted tree, table, list, or other pre-stringified data structire using the system
    pager, with colored unicode formatting and optional additional coloring

    Args:
        diagram (str): Stringified diagram, as a block of text
        highlight_strs (list): Additional specific strings to be highlighted
        \\*\\*echo_args (dict): Optional arguments to :py:func:`click.echo`
    """
    # Correctly handle horizontal paging and terminal control characters (for color)
    original_less = os.environ.get('LESS', '')
    os.environ['LESS'] = original_less + (' --chop-long-lines'
                                          ' --quit-on-intr'
                                          ' --quit-if-one-screen'
                                          ' --RAW-CONTROL-CHARS'
                                          ' --no-init')

    click.echo_via_pager(format_diagram(diagram, highlight_strs), **echo_args)

    # Reset LESS
    os.environ['LESS'] = original_less


def print_diff_table(old_table, new_table, reset=True):
    """
    Print a dict as a table, highlighting the differences between it and another dict.
    Outputs to the system pager, with colored unicode formatting.

    Args:
        old_table (dict): Older dict used for comparison
        new_table (dict): Dict containing values to print
        reset (bool): Reset cursor position after printing, to redraw over the table
    """
    diff_table = new_table.copy()
    for key in new_table.keys():
        if old_table[key] != new_table[key]:
            diff_table[key] = click.style(text_type(new_table[key]), fg=CLI_SUCCESS)
    print_table([diff_table])
    if reset:
        move_cursor(6, 'up')


def print_list(l, highlight_strs=None):
    """
    Print a bulleted list.
    Outputs to the system pager, with colored unicode formatting

    Args:
        l (list): A list (or other collection) to format
        highlight_strs (list): Additional specific strings to be highlighted
    """
    formatted = '\n'.join(['• ' + line for line in l])
    print_diagram(formatted, highlight_strs=highlight_strs)


def print_table(table, headers='keys', highlight_strs=None, **echo_args):
    """
    Print a tabular collection.
    Outputs to the system pager, with colored unicode formatting

    Args:
        table: A nested dict or list of dicts, with keys representing columns
        headers (str): Header type to be used with :py:mod:`tabulate`
        highlight_strs (list): Additional specific strings to be highlighted
        \\*\\*echo_args (dict): Optional arguments to :py:func:`click.echo`
    """
    formatted = tabulate(table, headers=headers, tablefmt='fancy_grid')
    print_diagram(formatted, highlight_strs=highlight_strs, **echo_args)


def print_tree(tree, highlight_strs=None, **echo_args):
    """
    Print a tree structure (represented as a nested dictionary).
    Outputs to the system pager, with colored unicode formatting.

    Example:
        >>> tree = {
        >>>     'node_1': None,
        >>>     'node_2': 'node_2a',
        >>>     'node_3': {
        >>>         'node_3a': None,
        >>>         'node_3b': 'node_3b1'
        >>>      }
        >>> }
        >>> print_tree(tree)
        ┏━━• node_1
        ┣━━• node_2
        ┃  ┗━• node_2a
        ┗━━• node_3
            ┣━━• node_3a
            ┗━━• node_3b
                ┗━━• node_3b1

    Args:
        tree (dict): A nested dictionary representing a tree
        highlight_strs (list): Additional specific strings to be highlighted
        \\*\\*echo_args (dict): Optional arguments to :py:func:`click.echo`
    """
    formatted = '\n'.join(format_tree(tree, depth=0))
    print_diagram(formatted, highlight_strs=highlight_strs, **echo_args)


def format_tree(tree, depth):
    """
    Recursive function to format a nested dict as a unicode tree diagram

    Args:
        tree (dict): A nested dictionary representing a tree
        depth (int): Recursive depth of tree

    Returns:
        list: A list of formatted table rows
    """
    # Base case: Parent node was a leaf
    if not tree:
        return ''
    # Base case: If a dict value is a string, treat as a single leaf node
    elif isinstance(tree, text_type):
        return ['┗━ ' + tree]
    # Recursive case: Append nodes at this depth of the (sub)tree, and recursively append children
    else:
        tree_rows = []
        for i, (node, children) in enumerate(sorted(tree.items()), 1):
            lst_node = (i == len(tree))
            fst_node = (i == 1 and depth == 0)
            tree_rows.append(('┗━━' if lst_node else ('┏━━' if fst_node else '┣━━')) + '• ' + node)
            tree_rows.extend([('   ' if lst_node else '┃  ') + child_node
                              for child_node in format_tree(children, depth + 1)])
        return tree_rows


def move_cursor(n, direction):
    """
    Move terminal cursor in a giver direction and distance. Only supports ANSI terminals.

    Args:
        n (int): Number of characters to move cursor
        direction (str): Direction to move cursor. One of ``'up', 'down', 'left'``, or ``'right'``.
    """
    directions = {'up': 'A', 'down': 'B', 'right': 'C', 'left': 'D'}
    click.echo('\033[{}{}'.format(n, directions[direction]))


def group(name=None, **attrs):
    """
    **[Decorator]**

    Create a new :py:class:`click.Group`  with a callback function. This otherwise works the same
    as :py:func:`click.command`, but with a custom command class with colored help text
    (:py:class:`HelpColorsGroup`).

    Args:
        name (str): Name of the command. This defaults to the function name.
        \\*\\*attrs: Optional arguments to :py:class:`click.Command`
    """
    for key, value in HELP_COLORS.items():
        attrs.setdefault(key, value)
    attrs.setdefault('cls', HelpColorsGroup)
    return click.command(name, **attrs)


def command(name=None, **attrs):
    """
    **[Decorator]**

    Create a new :py:class:`click.Command` with a callback function. This otherwise works the same
    as :py:func:`click.command`, but with a custom command class with colored help text
    (:py:class:`HelpColorsCommand`).

    Args:
        name (str): Name of the command. This defaults to the function name.
        \\*\\*attrs: Optional arguments to :py:class:`click.Command`
    """
    for key, value in HELP_COLORS.items():
        attrs.setdefault(key, value)
    attrs.setdefault('cls', HelpColorsCommand)
    return click.command(name, **attrs)


def print_progress_generator(progress_generator):
    """
    Uses the reprint to attempt and replace the terminal output characters for the progress bars.
    """
    with output(output_type='dict') as output_lines:
        fmt = '{status} {progress}'
        for progress in progress_generator:
            if 'id' in progress:
                output_lines[progress['id']] = fmt.format(status=progress.get('status', ''),
                                                          progress=progress.get('progress', ''))
            else:
                # try status first, then try stream
                line = progress.get('status', progress.get('stream'))
                click.echo(line)


def pretty(value, htchar='\t', lfchar='\n', indent=0):
    """
    Prints pretty json
    :param value:
    :param htchar:
    :param lfchar:
    :param indent:
    :return: pretty json
    """


    nlch = lfchar + htchar * (indent + 1)
    if type(value) == type(dict()) or type(value) == type(OrderedDict()):
        items = [
            nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return str('{%s}' % (','.join(items) + lfchar + htchar * indent)).replace('\'','"').replace(']"',']').replace('"[','[').replace('"{"','{"').replace('"}"','"}').replace('"[\'','[\'').replace('\']"','\']')

    elif type(value) == type(list()):
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        if items:
            items = sorted(items)
        [str(item) for item in sorted(items)]
        return str('[%s]' % (','.join(sorted(items)) + lfchar + htchar * indent)).replace('\'','"').replace(']"',']').replace('"[','[').replace('"{"','{"').replace('"}"','"}').replace('"[\'','[\'').replace('\']"','\']')

    elif type(value) is tuple:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in sorted(value)
        ]

        return str('(%s)' % (','.join(items) + lfchar + htchar * indent)).replace('\'','"').replace(']"',']').replace('"[','[').replace('"{"','{"').replace('"}"','"}').replace('"[\'','[\'').replace('\']"','\']')

    elif type(value) == type(newstr()):
        if value.startswith('['):
            my_json = eval((value.replace('\'','"')))
            my_new_list = []
            for my_it in sorted(my_json):
                my_new_list.append(str(my_it))
            return str('"'+str(my_new_list)+'"').replace(']"',']').replace('"[','[').replace('"{"','{"').replace('"}"','"}').replace('"[\'','[\'').replace('\']"','\']')

        return repr(str(value))

    else:
        return str(repr(str(value))).replace('\'','"').replace(']"',']').replace('"[','[').replace('"{"','{"').replace('"}"','"}').replace('"[\'','[\'').replace('\']"','\']')


