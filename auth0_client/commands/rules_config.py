import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Rule Configs')
def rule_configs():
    """ Connections """


rule_configs.help = highlight(rule_configs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@rule_configs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_config_variable_keys_for_rules(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_config_variable_keys_for_rules())

@rule_configs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--key', '-k', help=' The key of the rules config to remove ', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def remove_rules_config_for_given_key(
        ini,
        key,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.remove_rules_config_for_given_key(key))


@rule_configs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--key', '-k', help='The key of the rules config to set ', required=True)
@click.option('--body', '-b', help='body example: { "value": "MY_RULES_CONFIG_VALUE"}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def set_the_rules_config_for_a_given_key(
        ini,
        key,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.set_the_rules_config_for_a_given_key(key=key, body=body))



