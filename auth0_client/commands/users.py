import click

from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)



@group(short_help='Users')
def users():
    """ Connections """


users.help = highlight(users.help, ['Create:', 'Delete:', 'Update:'], 'green')

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_or_search_users(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.list_users()

@users.command()
def create_a_user():
    print('not configured yet')

@users.command()
def get_a_user():
    print('not configured yet')

@users.command()
def delete_a_user():
    print('not configured yet')

@users.command()
def update_a_user():
    print('not configured yet')

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_list_of_guardian_enrollments(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.get_list_of_guardian_enrollments(user_id)


@users.command()
def get_users_log_events():
    print('not configured yet')

@users.command()
def delete_a_users_multifactor_provider():
    print('not configured yet')

@users.command()
def unlink_a_user_identity():
    print('not configured yet')

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def generate_new_guardian_recovery_code(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.generate_new_user_guardian_recovery_code(user_id)

@users.command()
def link_a_user_account():
    print('not configured yet')

