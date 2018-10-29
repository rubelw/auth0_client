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



    connections = {}

    client = Auth0Client(auth_config())
    results = client.get_all_connections()

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            print(pretty(item))
            if 'name' in item and 'id' in item:
                connections[item['id']] = {}
                connections[item['id']]['name'] = item['name']
                if 'enabled_clients' in item:
                    connections[item['id']]['enabled_clients'] = []
                    for clnt in item['enabled_clients']:
                        if clnt in client_applications:
                            temp_dict = {}
                            temp_dict['client_id'] = clnt
                            temp_dict['client_name'] = client_applications[clnt]
                            connections[item['id']]['enabled_clients'].append(temp_dict)
                        else:
                            temp_dict={}
                            temp_dict['client_id'] = clnt
                            connections[item['id']]['enabled_clients'].append(temp_dict)

        print('########################')
        print('Connections')
        print('########################')
        print(pretty(connections))
    else:
        print('No connections')

except (KeyboardInterrupt, SystemExit):
    sys.exit()