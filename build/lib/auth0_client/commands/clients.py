import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Clients')
def clients():
    """ Clients """


clients.help = highlight(clients.help, ['Create:', 'Delete:', 'Update:'], 'green')

@clients.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_client_applications(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_all_client_applications())


@clients.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--client-id', '-c', help='client id', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', '-l', help='if the fields specified are to be included in the result', required=True, default=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_client_application(
        ini,
        client_id,
        fields,
        include_fields,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_a_client_application(id=client_id, fields=fields, include_fields=include_fields))

@clients.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-c', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_client_application(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_a_client_application(body=body))


@clients.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--application-id', '-a', help='application id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_client_application(
        ini,
        application_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_a_client_application(id=application_id))


@clients.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--application-id', '-a', help='application id', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_client_application(
        ini,
        application_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_a_client_application(id=application_id, body=body))

@clients.command()
def rotate_a_client_secret():
    print('not configured yet')