from __future__ import absolute_import, division, print_function
import inspect
import json
import sys
import math
from auth0.v3.authentication import GetToken
from auth0.v3.management import Users
from auth0.v3.management import ClientGrants
from auth0.v3.management import Clients
from auth0.v3.management import Connections
from auth0.v3.management import Tenants
from auth0.v3.management import Blacklists
from auth0.v3.management import EmailTemplates






def lineno():
    """Returns the current line number in our program."""
    return str(' - Auth0Client - line number: '+str(inspect.currentframe().f_back.f_lineno))


class Auth0Client:
    """
    Auth0Client
    """

    def __init__(self, config_block):
        """
        Initialize Auth0Client
        :param config_block:
        """

        self.debug = False
        self.domain = None
        self.client_id = None
        self.client_secret = None
        self.token = None

        if config_block:
            self._config = config_block
        else:
            logging.error('config block was garbage')
            raise SystemError

        if 'debug' in self._config:
            self.debug = self._config['debug']

        if 'domain' in self._config:
            self.domain = self._config['domain']

        if 'client_id' in self._config:
            self.client_id = self._config['client_id']

        if 'client_secret' in self._config:
            self.client_secret = self._config['client_secret']

        self.get_token()


    def get_token(self):

        try:

            get_token = GetToken(self.domain)

            token = get_token.client_credentials(self.client_id,
                                                 self.client_secret, 'https://{}/api/v2/'.format(self.domain))

            self.token =  token['access_token']
        except Exception as err:
            print('Problem getting token' + str(err))
            sys.exit(1)

    def list_users(self):
        if self.debug:
            print('command - list_users'+lineno())

        users_per_page = 10
        users = Users(self.domain, self.token)
        pages = math.ceil(users.list(per_page=0, search_engine='v3')['total'] / users_per_page)
        for page in range(pages):
            print(json.dumps(users.list(search_engine='v3',page=page, per_page=users_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_blacklist(self):
        if self.debug:
            print('command - get_blacklists'+lineno())

        blacklists = Blacklists(self.domain, self.token)

        print(json.dumps(blacklists.get(), sort_keys=True, indent=4, separators=(',',':')))

    def get_connections(self):
        if self.debug:
            print('command - get_connections'+lineno())

        connections_per_page = 10
        connections = Connections(self.domain, self.token)

        pages = math.ceil(len(connections.all()) / connections_per_page)
        for page in range(pages):
            print(json.dumps(connections.all(page=page, per_page=connections_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_tenants(self):
        if self.debug:
            print('command - get_tenant'+lineno())

        tenants = Tenants(self.domain, self.token)

        print(json.dumps(tenants.get(), sort_keys=True, indent=4, separators=(',',':')))


    def get_clients(self):
        if self.debug:
            print('command - get_clients'+lineno())

        clients_per_page = 10
        clients = Clients(self.domain, self.token)

        pages = math.ceil(len(clients.all()) / clients_per_page)
        for page in range(pages):
            print(json.dumps(clients.all(page=page, per_page=clients_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_client_grants(self):
        if self.debug:
            print('command - get_client_grants'+lineno())

        grants_per_page = 10
        grants = ClientGrants(self.domain, self.token)

        pages = math.ceil(len(grants.all()) / grants_per_page)
        for page in range(pages):
            print(json.dumps(grants.all(page=page, per_page=grants_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_user_log_events(self, id):
        if self.debug:
            print('command - get_user_log_events'+lineno())

        #users_per_page = 10
        users = Users(self.domain, self.token)
        response = users.get_log_events(user_id=id)
        print(json.dumps(response))

        logs_per_page = 10

        pages = math.ceil(len(users.get_log_events(user_id=id, page=0)) / logs_per_page)
        for page in range(pages):
            print(json.dumps(users.get_log_events(user_id=id, page=page, per_page=logs_per_page), sort_keys=True, indent=4, separators=(',',':')))

        #pages = math.ceil(users.list(per_page=0, search_engine='v3')['total'] / users_per_page)
        #for page in range(pages):
        #    print(json.dumps(users.list(search_engine='v3',page=page, per_page=users_per_page), sort_keys=True, indent=4, separators=(',',':')))

