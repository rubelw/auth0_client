"""
The command line interface to auth0

"""
from __future__ import absolute_import, division, print_function
import sys
import inspect
import click
import click_completion
from configparser import RawConfigParser
from auth0_client import Auth0Client




def lineno():
    """Returns the current line number in our program."""
    return str(' - auth0_client - line number: '+str(inspect.currentframe().f_back.f_lineno))



@click.group()
@click.version_option(version='0.0.1')
def cli():
    pass

##################
# Blacklists
##################


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_blacklist(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_blacklist()

##################
# Client Grants
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_client_grants(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_client_grants()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body of message', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_client_grant(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.create_client_grant(body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-g', help='grant id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_client_grant(
        ini,
        grant_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_client_grant(id=grant_id)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-g', help='grant id', required=True)
@click.option('--body', '-b', help='body of message', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_client_grant(
        ini,
        grant_id,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.update_client_grant(id=grant_id, body=body)

##################
# Clients
##################


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_client_applications(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_all_client_applications()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--client-id', '-c', help='client id', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', '-l', help='if the fields specified are to be included in the result', required=True, default=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_client_application(
        ini,
        client_id,
        fields,
        include_fields,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_a_client_application(id=client_id, fields=fields, include_fields=include_fields)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-c', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_client_application(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.create_a_client_application(body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--application-id', '-a', help='application id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_client_application(
        ini,
        application_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_a_client_application(id=application_id)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--application-id', '-a', help='application id', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_client_application(
        ini,
        application_id,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))
        client.update_a_client_application(id=application_id, body=body)



##################
# Connections
##################


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_connections(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_all_connections()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', '-l', help='if the fields specified are to be included in the result', required=True, default=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_connection(
        ini,
        connection_id,
        fields,
        include_fields,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_a_connection(id=connection_id, fields=fields, include_fields=include_fields)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_a_connection(
        ini,
        connection_id,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.update_a_connection(id=connection_id, body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_connection(
        ini,
        connection_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_a_connection(id=connection_id)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--user-email', '-e', help='user email', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_connection_user(
        ini,
        connection_id,
        user_email,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_a_connection_user(id=connection_id, email=user_email)



##################
# Custom Domains
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_custom_domains(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_custom_domains()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_new_custom_domain(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.create_new_custom_domain(body=body)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_custom_domain(
        ini,
        domain_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_custom_domain(id=domain_id)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_custom_domain(
        ini,
        domain_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_custom_domain(id=domain_id)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--domain-id', '-d', help='domain id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def verify_custom_domain(
        ini,
        domain_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.verify_custom_domain(id=domain_id)


##################
# Device Credentials
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='User id', required=True)
@click.option('--client-id', '-c', help='Client id', required=True)
@click.option('--credentials-type', '-t', help='Credentials type', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_device_credentials(
        ini,
        user_id,
        client_id,
        credentials_type,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_device_credentials(user_id=user_id, client_id=client_id, cred_type=credentials_type)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_device_public_key(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.create_device_public_key(body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--device-id', '-d', help='device id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_device_credentials(
        ini,
        device_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_device_credentials(id=device_id)


##################
# Email Templates
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_email_template(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.create_email_template(body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--template-name', '-t', help='template name', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_email_template(
        ini,
        template_name,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.update_email_template(name=template_name, body=body)


##################
# Emails
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve: name, enabled, settings fields', required=True)
@click.option('--include-fields', help='if the fields specified are to be excluded from the result,', required=False, is_flag=True, default=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_email_provider(
        ini,
        fields,
        include_fields,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_email_provider(fields=fields, include_fields=include_fields)


@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_email_provider(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_email_provider()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def udate_email_provider(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.update_email_provider(body=body)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def condigure_email_provider(
        ini,
        body,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.configure_email_provider(body=body)


##################
# Grants
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='User id', required=True)
@click.option('--client-id', '-c', help='Client id', required=True)
@click.option('--audience', '-a', help='Audience', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_grants(
        ini,
        user_id,
        client_id,
        audience,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_all_grants(user_id=user_id, client_id=client_id, audience=audience)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--grant-id', '-u', help='Grant id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_grant(
        ini,
        grant_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.delete_grant(id=grant_id)


##################
# Guardian
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_factors(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_factors()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_enrollment_templates(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_enrollment_templates()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_sns_factor_provider_config(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_sns_factor_provider_config()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_twilio_factor_provider_config(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_twilio_factor_provider_config()

##################
# Jobs
##################

##################
# Logs
##################
@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='auth0 user id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_user_log_events(
        ini,
        user_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_user_log_events(user_id)

##################
# Resource Servers
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_resource_servers(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_all_resource_servers()

##################
# Rules
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_rules(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_all_rules()

##################
# Rules Config
##################


##################
# Stats
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def active_users(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.active_users()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--past_number_of_days', '-d', help='past number of days', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def daily_stats(
        ini,
        past_number_of_days,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.daily_stats(days=past_number_of_days)

##################
# Tenants
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_tenants(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_tenants()

##################
# Tickets
##################


##################
# User Blocks
##################
@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_user_blocks(
        ini,
        user_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_user_blocks(user_id)


##################
# Users
##################
@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def list_users(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.list_users()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_user_guardian_enrollments(
        ini,
        user_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_list_of_guardian_enrollments(user_id)

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--user-id', '-u', help='user id', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def generate_new_user_guardian_recovery_code(
        ini,
        user_id,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.generate_new_user_guardian_recovery_code(user_id)

##################
# Users By Email
##################

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--email', '-e', help='user email', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def users_by_email(
        ini,
        email,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.user_by_email(email=email)

















@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
def version(version):
    """
    Get version
    :param version:
    :return:
    """
    myversion()




def myversion():
    '''
    Gets the current version
    :return: current version
    '''
    print('Version: ')

def get_config_dict(ini_file, debug):

    ini_data = read_config_info(ini_file)

    if debug:
        print('ini file is: ' + str(ini_data))

    config_dict = {}

    if ini_data['parameters']['domain']:
        config_dict['domain'] = ini_data['parameters']['domain']
    if ini_data['parameters']['id']:
        config_dict['client_id'] = ini_data['parameters']['id']
    if ini_data['parameters']['secret']:
        config_dict['client_secret'] = ini_data['parameters']['secret']

    return config_dict


def read_config_info(ini_file):
    """
    Read the INI file
    Args:
        ini_file - path to the file
    Returns:
        A dictionary of stuff from the INI file
    Exits:
        1 - if problems are encountered
    """
    try:
        config = RawConfigParser()
        config.optionxform = lambda option: option
        config.read(ini_file)
        the_stuff = {}
        for section in config.sections():
            the_stuff[str(section)] = {}
            for option in config.options(section):
                the_stuff[str(section)][str(option)] = str(config.get(section, option.replace('\n', '')))

        return the_stuff
    except Exception as wtf:
        logging.error('Exception caught in read_config_info(): {}'.format(wtf))
        traceback.print_exc(file=sys.stdout)
        return sys.exit(1)







