import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Tenants')
def tenants():
    """ Connections """


tenants.help = highlight(tenants.help, ['Create:', 'Delete:', 'Update:'], 'green')

@tenants.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_tenant_settings(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_tenants())


@tenants.command()
def update_tenant_settings():
    print('not configured yet')


