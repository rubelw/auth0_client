import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='User Blocks')
def user_blocks():
    """ Connections """


user_blocks.help = highlight(user_blocks.help, ['Create:', 'Delete:', 'Update:'], 'green')

@user_blocks.command()
def get_blocks_by_identifier():
    print('not configured yet')

@user_blocks.command()
def unblock_by_identifier():
    print('not configured yet')

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
def unblock_a_user():
    print('not configured yet')


