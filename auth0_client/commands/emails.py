import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Emails')
def emails():
    """ Connections """


emails.help = highlight(emails.help, ['Create:', 'Delete:', 'Update:'], 'green')

@emails.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve: name, enabled, settings fields', required=True)
@click.option('--include-fields', help='if the fields specified are to be excluded from the result,', required=False, is_flag=True, default=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_the_email_provider(
        ini,
        fields,
        include_fields,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    client.get_email_provider(fields=fields, include_fields=include_fields)

@emails.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def delete_the_email_provider(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.delete_email_provider()

@emails.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_the_email_provider(
        ini,
        body,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    client.update_email_provider(body=body)

@emails.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def configure_the_email_provider(
        ini,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    client.configure_email_provider(body=body)