#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *

try:
    users = {}

    client = Auth0Client(auth_config())

    #fields_list = [
    #    'name'
    #]

    #fields = multiple_choice('Select a list of fields to include or exclude', fields_list)
    #include_fields = yes_or_no('Do you want to fields to be excluded from results?')

    results = client.get_email_provider(include_fields=False, fields=None)
    results = json.loads(results.replace('\t', '').replace('\n', ''))
    print(pretty(results))


except (KeyboardInterrupt, SystemExit):
    sys.exit()
