import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Jobs')
def jobs():
    """ Connections """


jobs.help = highlight(jobs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--job-id', '-j', help='job id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_a_job(
        ini,
        job_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_a_job(job_id))

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--job-id', '-j', help='job id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_failed_job_error_details(
        ini,
        job_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_failed_job_error_details(job_id))

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--job-id', '-j', help='job id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_results_of_a_job(
        ini,
        job_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_results_of_a_jobs(job_id))

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"connection_id": "con_0000000000000001","format": "csv","limit": 5,"fields": [[{"name": "user_id"},{"name": "name"},{"name": "email"},{"name": "identities[0].connection","export_as": "provider"},{"name": "user_metadata.some_field"}]]}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_job_to_export_users(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_job_to_export_users(job_id))

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--users-file-path', '-u', help='path to users file to import', required=True)
@click.option('--connection-id', '-c', help='connection id', required=True)
@click.option('--upsert', help='Update user if already exists', required=False, is_flag=True)
@click.option('--external-id', '-e', help='external customer defined id', required=True)
@click.option('--send-completion-email', help='send a completion email', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_job_to_import_users(
        ini,
        users_file_path,
        connection_id,
        upsert,
        external_id,
        send_completion_email,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_job_to_import_users(connection_id=connection_id, file_obj=users_file_path, upsert=upsert))

@jobs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body example: {"user_id": "google-oauth2|1234","client_id": ""}', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def send_a_verify_email_address_email(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.send_a_verify_email_address_email(body))


