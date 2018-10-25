import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Stats')
def stats():
    """ Connections """


stats.help = highlight(stats.help, ['Create:', 'Delete:', 'Update:'], 'green')

@stats.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_active_users_count(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.active_users()

@stats.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--past_number_of_days', '-d', help='past number of days', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_daily_stats(
        ini,
        past_number_of_days,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    client.daily_stats(days=past_number_of_days)


