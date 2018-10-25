import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Resource Servers')
def resource_servers():
    """ Connections """


resource_servers.help = highlight(resource_servers.help, ['Create:', 'Delete:', 'Update:'], 'green')

@resource_servers.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_resource_servers(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.get_all_resource_servers()

@resource_servers.command()
def create_resource_server():
    print('not configured yet')

@resource_servers.command()
def get_resource_server_by_id():
    print('not configured yet')

@resource_servers.command()
def delete_resource_server():
    print('not configured yet')

@resource_servers.command()
def update_resource_server():
    print('not configured yet')



