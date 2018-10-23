"""
The command line interface to auth0

"""
from __future__ import absolute_import, division, print_function
import sys
import inspect
import click
from configparser import RawConfigParser
from auth0_client import Auth0Client



def lineno():
    """Returns the current line number in our program."""
    return str(' - auth0_client - line number: '+str(inspect.currentframe().f_back.f_lineno))



@click.group()
@click.version_option(version='0.0.1')
def cli():
    pass


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
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_clients(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_clients()

@cli.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_connections(
        ini,
        version,
        debug
    ):

    if version:
        myversion()
    else:
        client = Auth0Client(get_config_dict(ini, debug))

        client.get_connections()

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







