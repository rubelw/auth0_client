#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *

try:

    client = Auth0Client(auth_config())
    results = client.get_blacklist()

    if type(results) == type(str()):
        results = json.loads(results)

    if results:
        for item in results:
            print(item)
    else:
        print('No blacklisted tokens')



except (KeyboardInterrupt, SystemExit):
    sys.exit()
