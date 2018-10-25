"""
The command line interface to auth0

"""
from __future__ import absolute_import, division, print_function
from inspect import getmembers, ismodule
import inspect
import click_completion
import click
from click.core import MultiCommand
import auth0_client.commands as cmd_modules
from auth0_client import __version__
from auth0_client.cli_util import shmecho, group
from auth0_client.config import CLI_STATUS, CLI_VERSION

click_completion.init()


def lineno():
    """Returns the current line number in our program."""
    return str(' - auth0_client - line number: '+str(inspect.currentframe().f_back.f_lineno))

CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
    'token_normalize_func': lambda x: x.replace('-', '_'),
}

def check_version(ctx, _, value):
    """
    Print current version, and check for latest version

    :param ctx Application context object (click.Context)
    :param value Passed in by Click
    :return None
    """
    if not value or ctx.resilient_parsing:
        return

    # If version does not have a build number, it is a local development version
    v_current = ('v{}'.format(__version__) if __version__.count('.') > 1
                 else 'v{} (development)'.format(__version__))
    shmecho(['auth0_client ', '1'], [CLI_STATUS, CLI_VERSION])

    ctx.exit()

@group(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--version', is_flag=True, is_eager=True, expose_value=False,
              callback=check_version, help='Show the current version, and check for latest')
def auth0_client():
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def _add_subcommands():
    """
    Individual commands (and sub-commands) are encapsulated in separate files
    under /commands. Collect these command groups, and add them underneath the
    top-level command (dredge).
    """
    cmd_groups = [cmd
                  for _, module in getmembers(cmd_modules, ismodule)
                  for _, cmd in getmembers(module)
                  if isinstance(cmd, MultiCommand)]

    for cmd_group in cmd_groups:
        auth0_client.add_command(cmd_group)


_add_subcommands()


if __name__ == "__main__":
   auth0_client()




