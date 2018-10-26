import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Device Credentials')
def device_credentials():
    """ Connections """


device_credentials.help = highlight(device_credentials.help, ['Create:', 'Delete:', 'Update:'], 'green')

@device_credentials.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='User id', required=True)
@click.option('--client-id', '-c', help='Client id', required=True)
@click.option('--credentials-type', '-t', help='Credentials type', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', help='if the fields specified are to be excluded from the result,', required=False, is_flag=True, default=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_device_credentials(
        ini,
        user_id,
        client_id,
        credentials_type,
        fields,
        include_fields,
        debug
    ):

    fields = fields.split(',')

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_device_credentials(fields=fields, include_fields=include_fields, user_id=user_id, client_id=client_id, cred_type=credentials_type))


@device_credentials.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_device_public_key(
        ini,
        body,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_device_public_key(body=body))

@device_credentials.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--device-id', '-d', help='device id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_device_credential(
        ini,
        device_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_device_credentials(id=device_id))


