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
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"change_password": {"enabled": false,"html": ""},"guardian_mfa_page": {"enabled": false,"html": ""},"default_audience": "","default_directory": "","error_page": {"html": "","show_log_link": false,"url": "https://mycompany.org/error"},"flags": {"change_pwd_flow_v1": false,"enable_client_connections": false,"enable_apis_section": false,"enable_pipeline2": false,"enable_dynamic_client_registration": false,"enable_custom_domain_in_emails": false},"friendly_name": "My Company","picture_url": "https://mycompany.org/logo.png","support_email": "support@mycompany.org","support_url": "https://mycompany.org/support","allowed_logout_urls": ["https://mycompany.org/logoutCallback"],"session_lifetime": 168,"idle_session_lifetime": 72,"sandbox_version": "8"} ', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_tenant_settings(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_tenant_settings(body=body))


