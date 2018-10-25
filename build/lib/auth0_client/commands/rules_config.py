import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Rule Configs')
def rule_configs():
    """ Connections """


rule_configs.help = highlight(rule_configs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@rule_configs.command()
def list_config_variable_keys_for_rules():
    print('not configured yet')

@rule_configs.command()
def remove_rules_config_for_given_key():
    print('not configured yet')

@rule_configs.command()
def set_the_rules_config_for_a_given_key():
    print('not configured yet')




