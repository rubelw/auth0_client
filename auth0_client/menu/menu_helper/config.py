

from .pretty import *
import os
from os.path import expanduser





DEBUG=1

def create_auth0_client_menu_config_file():


    home = expanduser("~")

    PATH = home+'/.auth0-client/auth0_client.ini'

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        if (DEBUG):
            print("auth0 config file exists and is readable")

    else:
        print("Either file is missing or is not readable.  Let us create a file")

        open(PATH, 'w').close()




