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
        email = parts[1]

        send_mail= yes_or_no('Send email to user (Y/N)?')

        body={
            "user_id":id,
            "email": email,
            "send_mail":send_mail
        }
        results = client.create_a_guardian_enrollment_ticket(body=body)

        results= results.replace('\t','').replace('\n','')
        print(pretty(json.loads(results)))





except (KeyboardInterrupt, SystemExit):
    sys.exit()
