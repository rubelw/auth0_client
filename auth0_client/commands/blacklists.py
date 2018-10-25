import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)

@group(short_help='Blacklists')
def blacklists():
    """ Connections """


blacklists.help = highlight(blacklists.help, ['Create:', 'Delete:', 'Update:'], 'green')

@blacklists.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_blacklisted_tokens(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.get_blacklist()


@blacklists.command()
def blacklist_a_token():
    print('not configured yet')
