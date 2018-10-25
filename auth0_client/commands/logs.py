import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Logs')
def logs():
    """ Connections """


logs.help = highlight(logs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@logs.command()
def search_log_events():
    print('not configured yet')


@logs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='auth0 user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_log_event_by_id(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.get_user_log_events(user_id)





