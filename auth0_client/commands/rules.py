import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Rule')
def rules():
    """ Connections """


rules.help = highlight(rules.help, ['Create:', 'Delete:', 'Update:'], 'green')

@rules.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_rules(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.get_all_rules()


@rules.command()
def create_a_rule():
    print('not configured yet')

@rules.command()
def get_rule_by_id():
    print('not configured yet')

@rules.command()
def delete_rule():
    print('not configured yet')

@rules.command()
def update_rule():
    print('not configured yet')



