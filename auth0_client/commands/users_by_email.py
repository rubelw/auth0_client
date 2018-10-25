import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Users By Email')
def users_by_email():
    """ Connections """


users_by_email.help = highlight(users_by_email.help, ['Create:', 'Delete:', 'Update:'], 'green')

@users_by_email.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--email', '-e', help='user email', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def search_users_by_email(
        ini,
        email,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.user_by_email(email=email)






