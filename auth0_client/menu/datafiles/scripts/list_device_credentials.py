#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:

    ### Get guardian enrollments
    ### Can only get devices from users who are enrolled









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
            #print(l)
            #print(users[l])
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
        id = parts[2]





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
                #print('id: '+str(c))
                #print(pretty(client_applications[c]))
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






            types = [ 'public_key', 'refresh_token']
            type = multiple_choice('Select Credentials Type', types)


            fields_list = [ 'device_name,device_id,type,user_id']


            counter = 1
            menu = {}

            for field in fields_list:
                menu[counter] = str(field)
                counter += 1

            print("\n")
            print('#########################################')
            print('## ' + str('Select Fields') + ' ##')
            print('#########################################')
            for key in sorted(menu):
                print(str(key) + ":" + menu[key])

            pattern = r'^[0-9]+$'
            while True:
                ans = input("Make A Choice: [ENTER]")
                if re.match(pattern, ans) is not None:
                    if int(ans) in menu:
                        fields = menu[int(ans)]
                        break



            include_fields = yes_or_no('Include fields from results (Y/N)')


            results = client.get_device_credentials(cred_type=type, user_id=id, client_id=client_id, fields=str(fields), include_fields=include_fields)
            print(results)

        else:
            print('No client applications')

    else:
        print('No users')



except (KeyboardInterrupt, SystemExit):
    sys.exit()