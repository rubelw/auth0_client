#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:

    # Let's get all the clients first
    client_applications = {}

    client = Auth0Client(auth_config())
    results = client.get_all_client_applications()

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            if 'client_id' in item and 'name' in item:
                client_applications[item['client_id']] = item['name']





    client_grants = {}

    client = Auth0Client(auth_config())
    results = client.get_client_grants()

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            if 'client_id' in item and 'id' in item:
                client_grants[item['id']] = {}
                client_grants[item['id']]['client_id'] = item['client_id']
                if item['client_id'] in client_applications:
                    client_grants[item['id']]['client_name']= client_applications[item['client_id']]
                client_grants[item['id']]['audience']=item['audience']
                if 'scope' in item:
                    client_grants[item['id']]['scope']= item['scope']

        print('########################')
        print('Client Grants')
        print('########################')
        print(pretty(client_grants))
    else:
        print('No client grants')



except (KeyboardInterrupt, SystemExit):
    sys.exit()
