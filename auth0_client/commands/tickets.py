import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Tickets')
def tickets():
    """ Connections """


tickets.help = highlight(tickets.help, ['Create:', 'Delete:', 'Update:'], 'green')

@tickets.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"result_url": "http://myapp.com/callback","user_id": "", "ttl_sec": 0}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_an_email_verification_ticket(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_an_email_verification_ticket(body=body))

@tickets.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"result_url": "http://myapp.com/callback","user_id": "", "connection_id": "con_0000000000000001", "email": "","ttl_sec": 0}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_password_change_ticket(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_a_password_change_ticket(body=body))




