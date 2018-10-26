import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='User Blocks')
def user_blocks():
    """ Connections """


user_blocks.help = highlight(user_blocks.help, ['Create:', 'Delete:', 'Update:'], 'green')

@user_blocks.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--identifier', '-d', help=' Should be any of: username, phone_number, email.', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_blocks_by_identifier(
        ini,
        identifier,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_blocks_by_identifier(identifier))

@user_blocks.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--identifier', '-d', help=' Should be any of: username, phone_number, email.', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def unblock_by_identifier(
        ini,
        identifier,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.unblock_by_identifier(identifier))

@user_blocks.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_users_blocks(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_user_blocks(user_id))

@user_blocks.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='The user_id of the user to update.', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def unblock_a_user(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.unblock_a_user(user_id))



