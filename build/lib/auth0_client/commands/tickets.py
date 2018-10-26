import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Tickets')
def tickets():
    """ Connections """


tickets.help = highlight(tickets.help, ['Create:', 'Delete:', 'Update:'], 'green')

@tickets.command()
def create_an_email_verification_ticket():
    print('not configured yet')


@tickets.command()
def create_a_password_change_ticket():
    print('not configured yet')




