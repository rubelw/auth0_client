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
    print(client.get_all_rules())


@rules.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"name": "my-rule","script": "function (user, context, callback) {\n  callback(null, user, context);\n}","order": 2,"enabled": true}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_rule(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_all_rules())


@rules.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--rule-id', '-r', help='The id of the rule to retrieve', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', help='Turn on debugging', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_rule_by_id(
        ini,
        rule_id,
        fields,
        include_fields,
        debug
    ):

    field=fields.split.split(',')
    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_rule_by_id(id=rule_id,fields=fields, include_fields=include_fields))

@rules.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--rule-id', '-r', help='The id of the rule to delete', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_rule(
        ini,
        rule_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_rule(id=rule_id))

@rules.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--rule-id', '-r', help='The id of the rule to delete', required=True)
@click.option('--body', '-b', help='body example: {"script": "function (user, context, callback) {\n  callback(null, user, context);\n}","name": "my-rule","order": 2,"enabled": true} ', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_rule(
        ini,
        rule_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_rule(id=rule_id, body=body))



