#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:
    factors = {}

    client = Auth0Client(auth_config())
    results = client.list_factors()

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            print(pretty(item))

    else:
        print('No guardian factors or statuses')



except (KeyboardInterrupt, SystemExit):
    sys.exit()
