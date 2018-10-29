#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:

    enrollments = {}


    client = Auth0Client(auth_config())

    types = ['totp','sms','push','email','recovery-code']

    for my_type in types:
        print(my_type)
        results = client.get_a_guardian_enrollment(id=my_type)

        print(pretty(results))



    else:
        print('No users')





except (KeyboardInterrupt, SystemExit):
    sys.exit()
