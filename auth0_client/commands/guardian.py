import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Guardian')
def guardian():
    """ Connections """


guardian.help = highlight(guardian.help, ['Create:', 'Delete:', 'Update:'], 'green')

@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_list_of_factors_and_statuses(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_factors())

@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--enrollment-id', '-e', help='delete a guardian enrollment', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_guardian_enrollment(
        ini,
        enrollment_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_a_guardian_enrollment(id))


@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--enrollment-id', '-e', help='delete a guardian enrollment', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_a_guardian_enrollment(
        ini,
        enrollment_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.delete_a_guardian_enrollment(id))



@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_enrollment_and_verification_templates(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_enrollment_templates())



@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: { "enrollment_message": "{{code}} is your verification code for {{tenant.friendly_name}}. Please enter this code to verify your enrollment.","verification_message": "{{code}} is your verification code for {{tenant.friendly_name}}"}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_enrollment_and_verification_templates(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_enrollment_and_verification_templates(body=body))


@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_guardian_sns_factor_provider_configuration(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_sns_factor_provider_config())

@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_guardian_twilio_factor_provider_configuration(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.list_twilio_factor_provider_config())

@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"from": "+1223323",  "messaging_service_sid": "5dEkAiHLPCuQ1uJj4qNXcAnERFAL6cpq",  "auth_token": "zw5Ku6z2sxhd0ZVXto5SDHX6KPDByJPU",  "sid": "wywA2BH4VqTpfywiDuyDAYZL3xQjoO40"}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_guardians_twilio_sms_factor_provider(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_guardians_twilio_sms_factor_provider(body=body))


@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"user_id": "",  "email": "",  "send_mail": false}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_a_guardian_enrollment_ticket(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_a_guardian_enrollment_ticket(body=body))


@guardian.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--name', '-n', help='name', required=True)
@click.option('--body', '-b', help='body example: {"enabled": false}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_guardian_factor(
        ini,
        name,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_guardian_factor(name=name, body=body))