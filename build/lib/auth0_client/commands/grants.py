import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Grants')
def grants():
    """ Connections """


grants.help = highlight(grants.help, ['Create:', 'Delete:', 'Update:'], 'green')

@grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='User id', required=True)
@click.option('--client-id', '-c', help='Client id', required=True)
@click.option('--audience', '-a', help='Audience', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_grants(
        ini,
        user_id,
        client_id,
        audience,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_all_grants(user_id=user_id, client_id=client_id, audience=audience))



@grants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-u', help='Grant id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_grant(
        ini,
        grant_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_grant(id=grant_id))





