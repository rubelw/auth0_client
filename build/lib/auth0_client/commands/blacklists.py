import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)

@group(short_help='Blacklists')
def blacklists():
    """ Connections """


blacklists.help = highlight(blacklists.help, ['Create:', 'Delete:', 'Update:'], 'green')

@blacklists.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_all_blacklisted_tokens(
        ini,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_blacklist())


@blacklists.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--jwt-audit-claim', '-j', help='The JWT\'s aud claim. The client_id of the client for which it was issued', required=True)
@click.option('--jti', '-t', help='The jti of the JWT to blacklist', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def blacklist_a_token(
        ini,
        jwt_audit_claim,
        jti,
        debug
    ):

    body = {}
    body['aud'] = jwt_audit_claim
    body['jti'] = jti
    body = json.loads(data)
    client = Auth0Client(get_config_dict(ini, debug))
    print(client.blacklist_a_token(body=body))