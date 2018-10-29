#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:
    users = {}

    client = Auth0Client(auth_config())
    results = client.list_users()

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            print(pretty(item))
            if 'user_id' in item and 'email' in item:
                users[item['user_id']] = {}
                users[item['user_id']]['email'] = item['email']
                if 'name' in item:
                    users[item['user_id']]['name'] = item['name']


        print('########################')
        print('Users')
        print('########################')
        print(pretty(users))
    else:
        print('No users')



except (KeyboardInterrupt, SystemExit):
    sys.exit()
