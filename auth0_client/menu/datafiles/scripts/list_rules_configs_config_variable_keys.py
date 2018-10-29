#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:

    client = Auth0Client(auth_config())
    results = client.list_config_variable_keys_for_rules()

    if type(results) == type(str()):
        results = json.loads(results)

    if results:
        print(pretty(results))
    else:
        print('No config variable keys for rules')



except (KeyboardInterrupt, SystemExit):
    sys.exit()