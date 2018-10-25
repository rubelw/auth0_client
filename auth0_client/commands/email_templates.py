import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Email Templates')
def email_templates():
    """ Connections """


email_templates.help = highlight(email_templates.help, ['Create:', 'Delete:', 'Update:'], 'green')

@email_templates.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--template-name', '-t', help='template name', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_an_email_template(
        ini,
        template_name,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_an_email_template(name=template_name))


@email_templates.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--template-name', '-t', help='template name', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def update_an_email_template(
        ini,
        template_name,
        body,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.update_email_template(name=template_name, body=body))

@email_templates.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--body', '-b', help='body', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def create_an_email_template(
        ini,
        body,
        debug
    ):


    client = Auth0Client(get_config_dict(ini, debug))
    print(client.create_email_template(body=body))