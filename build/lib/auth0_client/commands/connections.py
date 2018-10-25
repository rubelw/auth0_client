import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Connections')
def connections():
    """ Connections """


connections.help = highlight(connections.help, ['Create:', 'Delete:', 'Update:'], 'green')

@connections.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_connections(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_all_connections())

@connections.command()
def create_a_connection():
    print('not configured yet')

@connections.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', '-l', help='if the fields specified are to be included in the result', required=True, default=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_connection(
        ini,
        connection_id,
        fields,
        include_fields,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_a_connection(id=connection_id, fields=fields, include_fields=include_fields))

@connections.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--user-email', '-e', help='user email', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_connection_user(
        ini,
        connection_id,
        user_email,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_a_connection_user(id=connection_id, email=user_email))

@connections.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_connection(
        ini,
        connection_id,
        body,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_a_connection(id=connection_id, body=body))

@connections.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_connection(
        ini,
        connection_id,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_a_connection(id=connection_id))