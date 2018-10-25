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
def get_a_guardian_enrollment():
    print('not configured yet')

@guardian.command()
def delete_a_guardian_enrollment():
    print('not configured yet')

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
def update_enrollment_and_verification_templates():
    print('not configured yet')

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
def update_guardians_twilio_sms_factor_provider():
    print('not configured yet')

@guardian.command()
def create_a_guardian_enrollment_ticket():
    print('not configured yet')

@guardian.command()
def update_guardian_factor():
    print('not configured yet')