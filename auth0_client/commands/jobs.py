import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Jobs')
def jobs():
    """ Connections """


jobs.help = highlight(jobs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@jobs.command()
def get_a_job():
    print('not configured yet')


@jobs.command()
def get_failed_job_error_details():
    print('not configured yet')

@jobs.command()
def get_results_of_a_job():
    print('not configured yet')

@jobs.command()
def create_job_to_export_users():
    print('not configured yet')

@jobs.command()
def create_job_to_import_users():
    print('not configured yet')

@jobs.command()
def send_a_verify_email_address_email():
    print('not configured yet')


