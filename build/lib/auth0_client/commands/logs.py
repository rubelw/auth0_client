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
@click.option('--log-id', '-u', help='log id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_log_event_by_id(
        ini,
        log_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_log_events_by_id(log_id))





