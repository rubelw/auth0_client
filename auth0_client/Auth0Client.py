from __future__ import absolute_import, division, print_function
import inspect
import json
import sys
import math
from time import strftime
from datetime import date, timedelta, datetime
from auth0.v3.authentication import GetToken
from auth0.v3.management import Users
from auth0.v3.management import ClientGrants
from auth0.v3.management import Clients
from auth0.v3.management import Connections
from auth0.v3.management import Tenants
from auth0.v3.management import Blacklists
from auth0.v3.management import UserBlocks
from auth0.v3.management import UsersByEmail
from auth0.v3.management import Stats
from auth0.v3.management import Guardian
from auth0.v3.management import Rules
from auth0.v3.management import ResourceServers
from auth0.v3.management import Grants
from auth0.v3.management import DeviceCredentials
from auth0.v3.management import CustomDomains


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
        Initialize Auth0Client and get a token
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

    ##################
    # Client Grants
    ##################

    def get_client_grants(self):
        if self.debug:
            print('command - get_client_grants'+lineno())

        grants_per_page = 10
        grants = ClientGrants(self.domain, self.token)

        pages = math.ceil(len(grants.all()) / grants_per_page)
        for page in range(pages):
            print(json.dumps(grants.all(page=page, per_page=grants_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def create_client_grant(self):
        if self.debug:
            print('command - create_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        print(json.dumps(grants.create(body=body), sort_keys=True, indent=4, separators=(',',':')))

    def delete_client_grant(self, id):
        if self.debug:
            print('command - delete_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        print(json.dumps(grants.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))


    def update_client_grant(self, id, body):
        if self.debug:
            print('command - update_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        print(json.dumps(grants.update(id=id, body=body), sort_keys=True, indent=4, separators=(',',':')))



    ##################
    # Clients
    ##################
    def get_all_client_applications(self):
        if self.debug:
            print('command - get_all_clients_applications'+lineno())

        clients_per_page = 10
        clients = Clients(self.domain, self.token)

        pages = math.ceil(len(clients.all()) / clients_per_page)
        for page in range(pages):
            print(json.dumps(clients.all(page=page, per_page=clients_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_a_client_application(self, id, fields, include_fields):
        if self.debug:
            print('command - get_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        print(json.dumps(clients.get(id=id, fields=fields, include_fields=include_fields), sort_keys=True, indent=4, separators=(',',':')))

    def create_a_client_application(self, body):
        if self.debug:
            print('command - create_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        print(json.dumps(clients.create(body=body), sort_keys=True, indent=4, separators=(',',':')))

    def delete_a_client_application(self, id):
        if self.debug:
            print('command - delete_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        print(json.dumps(clients.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))

    def update_a_client_application(self, id, body):
        if self.debug:
            print('command - update_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        print(json.dumps(clients.update(id=id, body=body), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Blacklists
    ##################
    def get_blacklist(self):
        if self.debug:
            print('command - get_blacklists'+lineno())

        blacklists = Blacklists(self.domain, self.token)

        print(json.dumps(blacklists.get(), sort_keys=True, indent=4, separators=(',',':')))

    ##################
    # Connections
    ##################
    def get_all_connections(self):
        if self.debug:
            print('command - get_connections'+lineno())

        connections_per_page = 10
        connections = Connections(self.domain, self.token)

        pages = math.ceil(len(connections.all()) / connections_per_page)
        for page in range(pages):
            print(json.dumps(connections.all(page=page, per_page=connections_per_page), sort_keys=True, indent=4, separators=(',',':')))

    def get_a_connection(self, id, fields, include_fields=True):
        if self.debug:
            print('command - get_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        print(json.dumps(connections.all(id=id, fields=fields, include_fields=include_fields), sort_keys=True, indent=4, separators=(',',':')))

    def update_a_connection(self, id, body):
        if self.debug:
            print('command - update_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        print(json.dumps(connections.all(id=id, body=body), sort_keys=True, indent=4, separators=(',',':')))

    def delete_a_connection(self, id):
        if self.debug:
            print('command - delete_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        print(json.dumps(connections.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))

    def delete_a_connection_user(self, id, email):
        if self.debug:
            print('command - delete_a_connection_user'+lineno())

        connections = Connections(self.domain, self.token)
        print(json.dumps(connections. delete_user_by_email(id=id, email=email), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Custom Domains
    ##################

    def  get_custom_domains(self):
        if self.debug:
            print('command - get_custom_domains'+lineno())

        domains = CustomDomains(self.domain, self.token)

        print(json.dumps(domains.get_all(), sort_keys=True, indent=4, separators=(',',':')))



    def  create_new_custom_domain(self, body):
        if self.debug:
            print('command - create_new_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)

        print(json.dumps(domains.create_new(body=body), sort_keys=True, indent=4, separators=(',',':')))


    def  get_custom_domain(self, id):
        if self.debug:
            print('command - get_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)

        print(json.dumps(domains.get_domain_by_id(id=id), sort_keys=True, indent=4, separators=(',',':')))


    def  delete_custom_domain(self, id):
        if self.debug:
            print('command - delete_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)

        print(json.dumps(domains.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))


    def  verify_custom_domain(self, id):
        if self.debug:
            print('command - verify_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)

        print(json.dumps(domains.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))




    ##################
    # Device Credentials
    ##################

    def  get_device_credentials(self, user_id, client_id, cred_type):
        if self.debug:
            print('command - get_device_credentials'+lineno())

        device = DeviceCredentials(self.domain, self.token)

        print(json.dumps(device.get(user_id=user_id, client_id=client_id, type=cred_type), sort_keys=True, indent=4, separators=(',',':')))

    def  create_device_public_key(self, body):
        if self.debug:
            print('command - create_device_public_key'+lineno())

        device = DeviceCredentials(self.domain, self.token)

        print(json.dumps(device.create(body=body), sort_keys=True, indent=4, separators=(',',':')))

    def  delete_device_credentials(self, id):
        if self.debug:
            print('command - delete_device_credentials'+lineno())

        device = DeviceCredentials(self.domain, self.token)

        print(json.dumps(device.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))

    ##################
    # Email templates
    ##################

    def  create_email_template(self, body):
        if self.debug:
            print('command - create_email_template'+lineno())

        template = EmailTemplates(self.domain, self.token)

        print(json.dumps(template.create(body=body), sort_keys=True, indent=4, separators=(',',':')))

    def  update_email_template(self, name, body):
        if self.debug:
            print('command - update_email_template'+lineno())

        template = EmailTemplates(self.domain, self.token)

        print(json.dumps(template.update(template_name=name, body=body), sort_keys=True, indent=4, separators=(',',':')))

    ##################
    # Emails
    ##################


    def  get_email_provider(self, fields, include_fields):
        if self.debug:
            print('command - get_email_provider'+lineno())

        emails = Emails(self.domain, self.token)

        print(json.dumps(emails.get(fields=fields, include_fields=include_fields), sort_keys=True, indent=4, separators=(',',':')))


    def  delete_email_provider(self):
        if self.debug:
            print('command - delete_email_provider'+lineno())

        emails = Emails(self.domain, self.token)

        print(json.dumps(emails.delete(), sort_keys=True, indent=4, separators=(',',':')))

    def  update_email_provider(self, body):
        if self.debug:
            print('command - update_email_provider'+lineno())

        emails = Emails(self.domain, self.token)

        print(json.dumps(emails.update(body=body), sort_keys=True, indent=4, separators=(',',':')))

    def  configure_email_provider(self, body):
        if self.debug:
            print('command - configure_email_provider'+lineno())

        emails = Emails(self.domain, self.token)

        print(json.dumps(emails.config(body=body), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Grants
    ##################

    def get_all_grants(self, user_id, client_id, audience):
        if self.debug:
            print('command - get_all_grants'+lineno())

        grants = Grants(self.domain, self.token)

        print(json.dumps(grants.get_all(), sort_keys=True, indent=4, separators=(',',':')))

    def delete_grant(self, id):
        if self.debug:
            print('command - delete grant'+lineno())

        grants = Grants(self.domain, self.token)

        print(json.dumps(grants.delete(id=id), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Guardian
    ##################

    def list_factors(self):
        if self.debug:
            print('command - list_factors'+lineno())

        guardian = Guardian(self.domain, self.token)

        print(json.dumps(guardian.all_factors(), sort_keys=True, indent=4, separators=(',',':')))


    def list_enrollment_templates(self):
        if self.debug:
            print('command - list_enrollment_templates'+lineno())

        guardian = Guardian(self.domain, self.token)

        print(json.dumps(guardian.get_templates(), sort_keys=True, indent=4, separators=(',',':')))


    def list_sns_factor_provider_config(self):
        if self.debug:
            print('command - list_sns_factor_provider_config'+lineno())

        guardian = Guardian(self.domain, self.token)

        print(json.dumps(guardian.get_factor_providers(factor_name='push-notification',name='sns'), sort_keys=True, indent=4, separators=(',',':')))

    def list_twilio_factor_provider_config(self):
        if self.debug:
            print('command - list_twilio_factor_provider_config'+lineno())

        guardian = Guardian(self.domain, self.token)
        print(json.dumps(guardian.get_twilio_factor_provider_configuration(factor_name='sms', name='twileo'), sort_keys=True, indent=4, separators=(',',':')))




    ##################
    # Jobs
    ##################

    ##################
    # Logs
    ##################

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


    ##################
    # Resource Servers
    ##################
    def get_all_resource_servers(self):
        if self.debug:
            print('command - get_all_resource_servers'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)

        print(json.dumps(resourceservers.get_all(), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Rules
    ##################

    def get_all_rules(self):
        if self.debug:
            print('command - get_all_rules'+lineno())

        rules = Rules(self.domain, self.token)

        print(json.dumps(rules.all(), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Rules Configs
    ##################

    ##################
    # Stats
    ##################
    def active_users(self):
        if self.debug:
            print('command - active_users'+lineno())

        stats = Stats(self.domain, self.token)

        print(json.dumps(stats.active_users(), sort_keys=True, indent=4, separators=(',',':')))

    def daily_stats(self,days):
        if self.debug:
            print('command - daily_stats'+lineno())

        stats = Stats(self.domain, self.token)

        old_date = datetime.today() - timedelta(days=int(days))
        print(json.dumps(stats.daily_stats(from_date=old_date.strftime('%Y%m%d'), to_date=date.today().strftime('%Y%m%d')), sort_keys=True, indent=4, separators=(',',':')))


    ##################
    # Tenants
    ##################

    ##################
    # Tickets
    ##################

    ##################
    # User Blocks
    ##################

    ##################
    # Users
    ##################

    ##################
    # Users by email
    ##################


    ##################
    # Tenants
    ##################
    def get_tenants(self):
        if self.debug:
            print('command - get_tenant'+lineno())

        tenants = Tenants(self.domain, self.token)

        print(json.dumps(tenants.get(), sort_keys=True, indent=4, separators=(',',':')))



    ##################
    # Users
    ##################
    def list_users(self):
        if self.debug:
            print('command - list_users'+lineno())

        users_per_page = 10
        users = Users(self.domain, self.token)
        pages = math.ceil(users.list(per_page=0, search_engine='v3')['total'] / users_per_page)
        for page in range(pages):
            print(json.dumps(users.list(search_engine='v3',page=page, per_page=users_per_page), sort_keys=True, indent=4, separators=(',',':')))


    def get_list_of_guardian_enrollments(self, user_id=id):
        if self.debug:
            print('command - get_list_of_guardian_enrollments'+lineno())

        users = Users(self.domain, self.token)
        print(json.dumps(users.get_guardian_enrollments(user_id=user_id), sort_keys=True, indent=4, separators=(',',':')))


    def generate_new_user_guardian_recovery_code(self, user_id=id):
        if self.debug:
            print('command - generate_new_user_guardian_recovery_code'+lineno())

        users = Users(self.domain, self.token)
        print(json.dumps(users.regenerate_recovery_code(user_id=user_id), sort_keys=True, indent=4, separators=(',',':')))

    generate_new_user_guardian_recovery_code

    ##################
    # UserBlocks
    ##################
    def list_user_blocks(self, user_id):
        if self.debug:
            print('command - list_user_blocks'+lineno())

        blocks = UserBlocks(self.domain, self.token)

        print(json.dumps(blocks.get(id=user_id), sort_keys=True, indent=4, separators=(',',':')))

    ##################
    # Users By Email
    ##################

    def user_by_email(self,email):
        if self.debug:
            print('command - user_by_email'+lineno())

        users = UsersByEmail(self.domain, self.token)
        print(json.dumps(users.search_users_by_email(email=email), sort_keys=True, indent=4, separators=(',',':')))

