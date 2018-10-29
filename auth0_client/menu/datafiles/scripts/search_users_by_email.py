#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:
    users = {}

    email = single_question('Enter email to search for.')

    client = Auth0Client(auth_config())
    results = client.user_by_email(email=email)
    results = json.loads(results.replace('\t','').replace('\n',''))
    print(pretty(results))


except (KeyboardInterrupt, SystemExit):
    sys.exit()
