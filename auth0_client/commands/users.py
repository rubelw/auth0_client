import click

from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)



@group(short_help='Users')
def users():
    """ Connections """


users.help = highlight(users.help, ['Create:', 'Delete:', 'Update:'], 'green')

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_or_search_users(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_users())

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: { "user_id": "test",  "connection": "Username-Password-Authentication", "email": "john.doe@gmail.com",  "username": "johndoe",  "password": "secret12@%3AB",  "user_metadata": {},  "email_verified": false,  "verify_email": false,"app_metadata": {}}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_user(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_user(body=body))

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-d', help='User id', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', help='If fields specified should be included, default is True', required=False, is_flag=True, default=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_user(
        ini,
        user_id,
        fields,
        include_fields,
        debug
    ):

    fields= fields.split(',')
    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_a_user(id=user_id, fields=fields, include_fields=include_fields))

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_user(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_user(user_id=user_id))


@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--body', '-b', help='body example: {  "connection": "Username-Password-Authentication",  "email": "willrubel@gmail.com",  "user_metadata": {}}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_user(
        ini,
        user_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_user(id=user_id, body=body))




@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_list_of_guardian_enrollments(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_list_of_guardian_enrollments(user_id))


@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_users_log_events(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_user_log_eventss(user_id))

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--provider', '-p', help='provider', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_users_multifactor_provider(
        ini,
        user_id,
        provider,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_a_users_multifactor_provider(user_id, provider))

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--id', '-d', help='user id', required=True)
@click.option('--provider', '-p', help='The identity provider of the secondary linked account.  (Ex: 'google-oauth2' in google-oauth2|123456789081523216417)', required=True)
@click.option('--user-id', '-i', help='The unique identifier of the secondary linked account. (Only the id after the '|' pipe. Ex: '123456789081523216417' in google-oauth2|123456789081523216417)', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def unlink_a_user_identity(
        ini,
        id,
        provider,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.unlink_a_user_identity(id=id, provider=provider, user_id=user_id))


@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def generate_new_guardian_recovery_code(
        ini,
        user_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.generate_new_user_guardian_recovery_code(user_id))

@users.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--body', '-u', help='body example: {"provider": "twitter",  "connection_id": "",  "user_id": "191919191919191",  "link_with": "{SECONDARY_ACCOUNT_JWT}"}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def link_a_user_account(
        ini,
        user_id,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.generate_new_user_guardian_recovery_code(user_id))
