import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)

@group(short_help='ClientGroups')
def client_grants():
    """
    Create client grants.
    """
    pass


client_grants.help = highlight(client_grants.help, ['Create:', 'Delete:', 'Update:'], 'green')

@client_grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_client_grants(
        ini,
        debug
    ):
    client = Auth0Client(get_config_dict(ini, debug))
    client.get_client_grants()

@client_grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body of message', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_client_grant(
        ini,
        body,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    client.create_client_grant(body=body)


@client_grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-g', help='grant id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_client_grant(
        ini,
        grant_id,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    client.delete_client_grant(id=grant_id)


@client_grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-g', help='grant id', required=True)
@click.option('--body', '-b', help='body of message', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_client_grant(
        ini,
        grant_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.update_client_grant(id=grant_id, body=body)