import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Custom Domains')
def custom_domains():
    """ Connections """


custom_domains.help = highlight(custom_domains.help, ['Create:', 'Delete:', 'Update:'], 'green')

@custom_domains.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_custom_domain_configurations(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_custom_domains())

@custom_domains.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def configure_new_custom_domain(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_new_custom_domain(body=body))

@custom_domains.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_custom_domain_configuration(
        ini,
        domain_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_custom_domain(id=domain_id))


@custom_domains.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_custom_domain_configuration(
        ini,
        domain_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_custom_domain(id=domain_id))

@custom_domains.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def verify_a_custom_domain(
        ini,
        domain_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.verify_custom_domain(id=domain_id))

