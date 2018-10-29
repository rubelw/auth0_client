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
            if 'user_id' in item and 'email' in item:
                users[item['user_id']] = {}
                users[item['user_id']]['email'] = item['email']
                if 'name' in item:
                    users[item['user_id']]['name'] = item['name']
        counter = 1
        menu = {}

        for l in users:
            if 'name' in users[l]:
                menu[counter] = str(users[l]['name'])+' : '+str(users[l]['email'])+' : '+str(l)
            else:
                menu[counter] = str('unknown')+' : '+str(users[l]['email'])+' : '+str(l)

            counter += 1

        print("\n")
        print('#########################################')
        print('## '+str('Select User')+' ##')
        print('#########################################')
        for key in sorted(menu):
            print(str(key) + ":" + menu[key])


        pattern = r'^[0-9]+$'
        while True:
            ans = input("Make A Choice: [ENTER]")
            if re.match(pattern, ans) is not None:
                if int(ans) in menu:
                    answer = menu[int(ans)]
                    break

        parts = answer.replace(' ', '').split(':')
        user_id = parts[2]

        # Select the client
        client_applications = {}

        client = Auth0Client(auth_config())
        results = client.get_all_client_applications()

        if type(results) == type(str()):
            results = json.loads(results)

        if results:
            for item in results:
                if 'client_id' in item and 'name' in item:



                    client_applications[item['client_id']] = item['name']

            counter = 1
            menu = {}

            for c in client_applications:
                menu[counter] = str(client_applications[c]) + ' : ' + str(c)

                counter += 1

            print("\n")
            print('#########################################')
            print('## ' + str('Select Client') + ' ##')
            print('#########################################')
            for key in sorted(menu):
                print(str(key) + ":" + menu[key])

            pattern = r'^[0-9]+$'
            while True:
                ans = input("Make A Choice: [ENTER]")
                if re.match(pattern, ans) is not None:
                    if int(ans) in menu:
                        answer = menu[int(ans)]
                        break

            client_parts = answer.replace(' ', '').split(':')
            client_id = client_parts[1]

            audiences = []

            client = Auth0Client(auth_config())
            results = client.get_all_resource_servers()

            if type(results) == type(str()):
                results = json.loads(results)

            for aud in results:
                if 'identifier' in aud:
                    audiences.append(aud['identifier'])

            audience = multiple_choice('Select Audience', audiences)

            results = client.get_all_grants(user_id=user_id, client_id=client_id, audience=audience)
            if type(results) == type(str()):
                results = json.loads(results)

            print(pretty(results))


        else:
            print('No client applications')

    else:
        print('No users')



except (KeyboardInterrupt, SystemExit):
    sys.exit()