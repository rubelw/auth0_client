#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:
    users = {}


    days = single_question('Enter the number of days since today which you want to search')

    client = Auth0Client(auth_config())
    results = client.daily_stats(days=days)

    results=json.loads(results.replace('\t','').replace('\n',''))
    print(pretty(results))

except (KeyboardInterrupt, SystemExit):
    sys.exit()
