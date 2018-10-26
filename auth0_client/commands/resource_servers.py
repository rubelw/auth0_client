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
    print(client.get_all_resource_servers())

@resource_servers.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"name": "","identifier": "","scopes": ["object"],"signing_alg": "","signing_secret": "","allow_offline_access": false,"token_lifetime": 0,"skip_consent_for_verifiable_first_party_clients": false,"verificationLocation": "","options": {}}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_resource_server(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_resource_server(body=body))

@resource_servers.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--resource-id', '-r', help='The id or audience of the resource server to retrieve', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_resource_server_by_id(
        ini,
        resource_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_resource_server_by_id(id=resource_id))


@resource_servers.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--resource-id', '-r', help='The id or audience of the resource server to retrieve', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_resource_server(
        ini,
        resource_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_resource_server(id=resource_id))


@resource_servers.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--resource-id', '-r', help='The id or audience of the resource server to retrieve', required=True)
@click.option('--resource-id', '-r', help='body example: {"name": "","scopes": ["object"],"signing_alg": "","signing_secret": "","skip_consent_for_verifiable_first_party_clients": false,"allow_offline_access": false,"token_lifetime": 0,"verificationLocation": "","options": {}}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_resource_server(
        ini,
        resource_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_resource_server(id=resource_id, body=body))




