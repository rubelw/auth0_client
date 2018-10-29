#!/usr/bin/env python

import json
from auth0_client.Auth0Client import Auth0Client
from auth0_client.menu.menu_helper.common import *
from auth0_client.menu.menu_helper.pretty import *


try:
    client_applications = {}

    app_type = [
        'all',
        'native',
        'spa',
        'regular_web',
        'non_interactive',
        'rms',
        'box',
        'cloudbees',
        'concur',
        'dropbox',
        'mscrm',
        'echosign',
        'egnyte',
        'newrelic',
        'office365',
        'salesforce',
        'sentry',
        'sharepoint',
        'slack',
        'springcm',
        'zendesk',
        'zoom'
    ]

    selected_app = multiple_choice('Select Application Type', app_type)

    if selected_app == 'all':
        selected_app = None

    global_app = yes_or_no('Filter on the global client parameters? (Y/N)')


    first_party = yes_or_no('Filter on whether or not a client is a first party client? (Y/N)')


    client = Auth0Client(auth_config())
    results = client.get_all_client_applications(first_party=first_party, app_type=selected_app, is_global=global_app)

    if type(results) == type(str()):
        results = json.loads(results)


    if results:
        for item in results:
            print(pretty(item))
            if 'client_id' in item and 'name' in item:
                client_applications[item['client_id']] = item['name']

        print('########################')
        print('Client Applications')
        print('########################')
        print(pretty(client_applications))
    else:
        print('No client applications')



except (KeyboardInterrupt, SystemExit):
    sys.exit()
