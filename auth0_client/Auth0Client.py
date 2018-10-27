from __future__ import absolute_import, division, print_function
import inspect
import json
import sys
import math
from time import strftime
from datetime import date, timedelta, datetime
from auth0_client.v3.authentication import GetToken
from auth0_client.v3.management import Users
from auth0_client.v3.management import ClientGrants
from auth0_client.v3.management import Clients
from auth0_client.v3.management import Connections
from auth0_client.v3.management import Tenants
from auth0_client.v3.management import Blacklists
from auth0_client.v3.management import UserBlocks
from auth0_client.v3.management import UsersByEmail
from auth0_client.v3.management import Stats
from auth0_client.v3.management import Guardian
from auth0_client.v3.management import Rules
from auth0_client.v3.management import RulesConfigs
from auth0_client.v3.management import ResourceServers
from auth0_client.v3.management import Grants
from auth0_client.v3.management import DeviceCredentials
from auth0_client.v3.management import CustomDomains
from auth0_client.v3.management import EmailTemplates
from auth0_client.v3.management import Jobs
from auth0_client.v3.management import Tickets
from auth0_client.v3.management import Emails
from auth0_client.v3.management import Logs



from auth0_client.cli_util import (pretty)


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
    # Blacklists
    ##################
    def get_blacklist(self):
        if self.debug:
            print('command - get_blacklists'+lineno())

        blacklists = Blacklists(self.domain, self.token)

        return pretty(blacklists.get())

    def blacklist_a_token(self, body):
        if self.debug:
            print('command - blacklist a token'+lineno())

        blacklists = Blacklists(self.domain, self.token)

        return pretty(blacklists.create())

    ##################
    # Client Grants
    ##################

    def get_client_grants(self):
        if self.debug:
            print('command - get_client_grants'+lineno())

        grant_data = []
        grants_per_page = 10
        grants = ClientGrants(self.domain, self.token)

        pages = math.ceil(len(grants.all()) / grants_per_page)
        for page in range(pages):

            results = grants.all(page=page, per_page=grants_per_page)

            for data in results:
                grant_data.append(data)

        return pretty(grant_data)

    def create_client_grant(self, body):
        if self.debug:
            print('command - create_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        return pretty(grants.create(body=body))

    def delete_client_grant(self, id):
        if self.debug:
            print('command - delete_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        return pretty(grants.delete(id=id))

    def update_client_grant(self, id, body):
        if self.debug:
            print('command - update_client_grant'+lineno())

        grants = ClientGrants(self.domain, self.token)
        return pretty(grants.update(id=id, body=body))

    ##################
    # Clients
    ##################
    def get_all_client_applications(self):
        if self.debug:
            print('command - get_all_clients_applications'+lineno())

        client_data = []
        clients_per_page = 10
        clients = Clients(self.domain, self.token)

        pages = math.ceil(len(clients.all()) / clients_per_page)
        for page in range(pages):

            results = clients.all(page=page, per_page=clients_per_page)

            for client in results:
                client_data.append(client)

        return client_data

    def get_a_client_application(self, id, fields, include_fields):
        if self.debug:
            print('command - get_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        return pretty(clients.get(id=id, fields=fields, include_fields=include_fields))

    def create_a_client_application(self, body):
        if self.debug:
            print('command - create_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        return pretty(clients.create(body=body))

    def delete_a_client_application(self, id):
        if self.debug:
            print('command - delete_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        return pretty(clients.delete(id=id))

    def update_a_client_application(self, id, body):
        if self.debug:
            print('command - update_a_client_application'+lineno())

        clients = Clients(self.domain, self.token)
        return pretty(clients.update(id=id, body=body))

    ##################
    # Connections
    ##################
    def get_all_connections(self):
        if self.debug:
            print('command - get_connections'+lineno())

        connection_data = []
        connections_per_page = 10
        connections = Connections(self.domain, self.token)

        pages = math.ceil(len(connections.all()) / connections_per_page)
        for page in range(pages):
            results = connections.all(page=page, per_page=connections_per_page)

            for connection in results:
                connection_data.append(connection)

        return pretty(connection_data)

    def get_a_connection(self, id, fields, include_fields=True):
        if self.debug:
            print('command - get_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        return pretty(connections.get(id=id, fields=fields, include_fields=include_fields))

    def update_a_connection(self, id, body):
        if self.debug:
            print('command - update_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        return pretty(connections.update(id=id, body=body))

    def delete_a_connection(self, id):
        if self.debug:
            print('command - delete_a_connection'+lineno())

        connections = Connections(self.domain, self.token)
        return pretty(connections.delete(id=id))

    def delete_a_connection_user(self, id, email):
        if self.debug:
            print('command - delete_a_connection_user'+lineno())

        connections = Connections(self.domain, self.token)
        return pretty(connections. delete_user_by_email(id=id, email=email))

    ##################
    # Custom Domains
    ##################

    def get_custom_domains(self):
        if self.debug:
            print('command - get_custom_domains'+lineno())

        domains = CustomDomains(self.domain, self.token)
        return pretty(domains.get_all())


    def create_new_custom_domain(self, body):
        if self.debug:
            print('command - create_new_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)
        return pretty(domains.create_new(body=body))

    def get_custom_domain(self, id):
        if self.debug:
            print('command - get_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)
        return pretty(domains.get_domain_by_id(id=id))

    def delete_custom_domain(self, id):
        if self.debug:
            print('command - delete_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)
        return pretty(domains.delete(id=id))

    def verify_custom_domain(self, id):
        if self.debug:
            print('command - verify_custom_domain'+lineno())

        domains = CustomDomains(self.domain, self.token)
        return pretty(domains.verify(id=id))

    ##################
    # Device Credentials
    ##################

    def get_device_credentials(self, user_id, client_id, cred_type, fields, include_fields):
        if self.debug:
            print('command - get_device_credentials'+lineno())

        device = DeviceCredentials(self.domain, self.token)
        return pretty(device.get(fields=fields, include_fields=include_fields, user_id=user_id, client_id=client_id, type=cred_type))

    def create_device_public_key(self, body):
        if self.debug:
            print('command - create_device_public_key'+lineno())

        device = DeviceCredentials(self.domain, self.token)
        return pretty(device.create(body=body))

    def delete_device_credentials(self, id):
        if self.debug:
            print('command - delete_device_credentials'+lineno())

        device = DeviceCredentials(self.domain, self.token)
        return pretty(device.delete(id=id))

    ##################
    # Email templates
    ##################

    def create_email_template(self, body):
        if self.debug:
            print('command - create_email_template'+lineno())

        template = EmailTemplates(self.domain, self.token)
        return pretty(template.create(body=body))

    def update_email_template(self, name, body):
        if self.debug:
            print('command - update_email_template'+lineno())

        template = EmailTemplates(self.domain, self.token)
        return pretty(template.update(template_name=name, body=body))

    def get_an_email_template(self, name):
        if self.debug:
            print('command - get_an_email_template'+lineno())

        template = EmailTemplates(self.domain, self.token)
        return pretty(template.get(template_name=name))

    ##################
    # Emails
    ##################


    def get_email_provider(self, fields, include_fields):
        if self.debug:
            print('command - get_email_provider'+lineno())

        emails = Emails(self.domain, self.token)
        return pretty(emails.get(fields=fields, include_fields=include_fields))

    def delete_email_provider(self):
        if self.debug:
            print('command - delete_email_provider'+lineno())

        emails = Emails(self.domain, self.token)
        return pretty(emails.delete())

    def update_email_provider(self, body):
        if self.debug:
            print('command - update_email_provider'+lineno())

        emails = Emails(self.domain, self.token)
        return pretty(emails.update(body=body))

    def configure_email_provider(self, body):
        if self.debug:
            print('command - configure_email_provider'+lineno())

        emails = Emails(self.domain, self.token)
        return pretty(emails.config(body=body))

    ##################
    # Grants
    ##################

    def get_all_grants(self, user_id, client_id, audience):
        if self.debug:
            print('command - get_all_grants'+lineno())

        grants = Grants(self.domain, self.token)
        return pretty(grants.get_all())

    def delete_grant(self, id):
        if self.debug:
            print('command - delete grant'+lineno())

        grants = Grants(self.domain, self.token)
        return pretty(grants.delete(id=id))

    ##################
    # Guardian
    ##################

    def delete_a_guardian_enrollment(self, id):
        if self.debug:
            print('command - delete_a_guardian_enrollment'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.delete_enrollment(id=id))


    def list_factors(self):
        if self.debug:
            print('command - list_factors'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.all_factors())

    def list_enrollment_templates(self):
        if self.debug:
            print('command - list_enrollment_templates'+lineno())

        guardian = Guardian(self.domain, self.token)

        return pretty(guardian.get_templates())

    def list_sns_factor_provider_config(self):
        if self.debug:
            print('command - list_sns_factor_provider_config'+lineno())

        guardian = Guardian(self.domain, self.token)

        return pretty(guardian.get_factor_providers(factor_name='push-notification',name='sns'))

    def list_twilio_factor_provider_config(self):
        if self.debug:
            print('command - list_twilio_factor_provider_config'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.get_factor_providers(factor_name='sms', name='twilio'))


    def update_enrollment_and_verification_templates(self, body):
        if self.debug:
            print('command - update_enrollment_and_verification_template'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.update_templates(body=body))

    def update_guardians_twilio_sms_factor_provider(self, body):
        if self.debug:
            print('command - update_guardians_twilio_sms_factor_provider'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.update_factor_providers(factor_name='sms', name='twilio', body=body))

    def create_a_guardian_enrollment_ticket(self, body):
        if self.debug:
            print('command - create_a_guardian_enrollment_ticket'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.create_enrollment_ticket(body=body))

    def update_guardian_factor(self, name, body):
        if self.debug:
            print('command - update_guardian_factor'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.update_factor_providers(body=body))

    def get_a_guardian_enrollment(self, id):
        if self.debug:
            print('command - get_a_guardian_enrollment'+lineno())

        guardian = Guardian(self.domain, self.token)
        return pretty(guardian.get_enrollment(id=id))

    ##################
    # Jobs
    ##################

    def get_a_job(self, id):
        if self.debug:
            print('command - get_a_job'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.get(id=id))

    def get_failed_job_error_details(self, id):
        if self.debug:
            print('command - get_failed_job_error_details'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.get_failed_job(id=id))

    def get_results_of_a_job(self, id):
        if self.debug:
            print('command - get_results_of_a_job'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.get_job_results(id=id))

    def create_job_to_export_users(self, body):
        if self.debug:
            print('command - create_job_to_export_users'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.export_users(id=id))

    def create_job_to_import_users(self, connection_id, upsert, file_obj):
        if self.debug:
            print('command - create_job_to_import_users'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.import_users(connection_id=connection_id,file_obj=file_obj,upsert=upsert))

    def send_a_verify_email_address_email(self, body):
        if self.debug:
            print('command - send_a_verify_email_address_email'+lineno())

        jobs = Jobs(self.domain, self.token)
        return pretty(jobs.send_verification_email(body=body))

    ##################
    # Logs
    ##################

    def get_log_events_by_id(self, id):
        if self.debug:
            print('command - get_log_events_by_id'+lineno())

        logs = Logs(self.domain, self.token)
        return pretty(logs.get(id=id))

    def search_log_events(
            self,
            page,
            per_page,
            sort,
            fields,
            include_fields,
            include_totals,
            from_id,
            take,
            query
    ):
        if self.debug:
            print('command - search_log_events'+lineno())

        logs = Logs(self.domain, self.token)
        return pretty(logs.search(
            page=page,
            per_page=per_page,
            sort=sort,
            q=query,
            include_totals=include_totals,
            fields=fields,
            from_param=from_id,
            take = take
        ))



    ##################
    # Resource Servers
    ##################
    def get_all_resource_servers(self):
        if self.debug:
            print('command - get_all_resource_servers'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)
        return pretty(resourceservers.get_all())

    def create_resource_server(self, body):
        if self.debug:
            print('command - create_resource_server'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)
        return pretty(resourceservers.create(body=body))

    def get_resource_server_by_id(self, id):
        if self.debug:
            print('command - get_resource_server_by_id'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)
        return pretty(resourceservers.get(id=id))

    def delete_resource_server(self, id):
        if self.debug:
            print('command - delete_resource_server'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)
        return pretty(resourceservers.delete(id=id))

    def update_resource_server(self, id, body):
        if self.debug:
            print('command - update_resource_server'+lineno())

        resourceservers = ResourceServers(self.domain, self.token)
        return pretty(resourceservers.update(id=id, body=body))

    ##################
    # Rules
    ##################

    def get_all_rules(self):
        if self.debug:
            print('command - get_all_rules'+lineno())

        rules = Rules(self.domain, self.token)
        return pretty(rules.all())

    def create_a_rule(self, body):
        if self.debug:
            print('command - create_a_rule'+lineno())

        rules = Rules(self.domain, self.token)
        return pretty(rules.create(body=body))

    def get_rule_by_id(self, id, fields, include_fields):
        if self.debug:
            print('command - get_rule_by_id'+lineno())

        rules = Rules(self.domain, self.token)
        return pretty(rules.get(id=id, fields=fields, include_fields=include_fields))

    def delete_rule(self, id):
        if self.debug:
            print('command - delete_rule'+lineno())

        rules = Rules(self.domain, self.token)
        return pretty(rules.delete(id=id))

    def update_rule(self, id, body):
        if self.debug:
            print('command - update_rule'+lineno())

        rules = Rules(self.domain, self.token)
        return pretty(rules.update(id=id, body=body))

    ##################
    # Rules Configs
    ##################

    def list_config_variable_keys_for_rules(self):
        if self.debug:
            print('command - list_config_variable_keys_for_rules'+lineno())

        rules = RulesConfigs(self.domain, self.token)
        return pretty(rules.all())

    def remove_rules_config_for_given_key(self,key):
        if self.debug:
            print('command - remove_rules_config_for_given_key'+lineno())

        rules = RulesConfigs(self.domain, self.token)
        return pretty(rules.remove(key))

    def set_the_rules_config_for_a_given_key(self,key, body):
        if self.debug:
            print('command - set_the_rules_config_for_a_given_key'+lineno())

        rules = RulesConfigs(self.domain, self.token)
        return pretty(rules.set_rule_for_key(key=key, body=body))


    ##################
    # Stats
    ##################
    def active_users(self):
        if self.debug:
            print('command - active_users'+lineno())

        stats = Stats(self.domain, self.token)
        return pretty(stats.active_users())

    def daily_stats(self,days):
        if self.debug:
            print('command - daily_stats'+lineno())

        stats = Stats(self.domain, self.token)

        old_date = datetime.today() - timedelta(days=int(days))
        return pretty(stats.daily_stats(from_date=old_date.strftime('%Y%m%d'), to_date=date.today().strftime('%Y%m%d')))

    ##################
    # Tenants
    ##################
    def get_tenants(self):
        if self.debug:
            print('command - get_tenant'+lineno())

        tenants = Tenants(self.domain, self.token)
        return pretty(tenants.get())

    def update_tenant_settings(self, body):
        if self.debug:
            print('command - update_tenant_settings'+lineno())

        tenants = Tenants(self.domain, self.token)
        return pretty(tenants.update(body=body))

    ##################
    # Tickets
    ##################

    def create_an_email_verification_ticket(self, body):
        if self.debug:
            print('command - create_an_email_verification_ticket'+lineno())

        tickets = Tickets(self.domain, self.token)
        return pretty(tickets.create_email_verification(body=body))

    def create_a_password_change_ticket(self, body):
        if self.debug:
            print('command - create_a_password_change_ticket'+lineno())

        tickets = Tickets(self.domain, self.token)
        return pretty(tickets.create_pswd_change(body=body))


    ##################
    # Users
    ##################
    def list_users(self):
        if self.debug:
            print('command - list_users'+lineno())

        user_data = []
        users_per_page = 10
        users = Users(self.domain, self.token)
        pages = math.ceil(users.list(per_page=0, search_engine='v3')['total'] / users_per_page)

        total_users = int(pages)*int(users_per_page)
        acceptable_number_of_pages = math.ceil(1000 / int(users_per_page))


        if self.debug:
            print('number of pages: '+str(pages))
            print('total_users: '+str(total_users))
            print('acceptable number of pages: '+str(acceptable_number_of_pages))

        if pages > acceptable_number_of_pages:
            pages = acceptable_number_of_pages -1

            print("\n##############################")
            print('Limited to a 1000 users by the api')
            print("#################################\n")


        if self.debug:
            pages=1

        for page in range(pages):
            results = users.list(search_engine='v3',page=page, per_page=users_per_page)

            if 'users' in results:
                for user in results['users']:
                    user_data.append(user)

        return pretty(user_data)


    def get_list_of_guardian_enrollments(self, user_id):
        if self.debug:
            print('command - get_list_of_guardian_enrollments'+lineno())

        users = Users(self.domain, self.token)
        results = users.get_guardian_enrollments(user_id=user_id)
        return pretty(results)


    def generate_new_user_guardian_recovery_code(self, user_id):
        if self.debug:
            print('command - generate_new_user_guardian_recovery_code'+lineno())

        users = Users(self.domain, self.token)
        return pretty(users.regenerate_recovery_code(user_id=user_id))

    def get_user_log_events(self, user_id):
        if self.debug:
            print('command - get_user_log_events'+lineno())
            print('user_id: '+str(user_id))

        log_data = []
        logs_per_page = 10
        users = Users(self.domain, self.token)
        pages = math.ceil(len(users.get_log_events(user_id=user_id, per_page=0)) / logs_per_page)
        for page in range(pages):
            results = users.get_log_events(user_id=user_id,page=page, per_page=logs_per_page)


            for log in results:
                log_data.append(log)

        return pretty(log_data)


    def delete_user(self, user_id):
        if self.debug:
            print('command - delete'+lineno())

        users = Users(self.domain, self.token)
        results = users.delete(id=user_id)
        return pretty(results)


    def delete_a_users_multifactor_provider(self, user_id, provider):
        if self.debug:
            print('command - delete user multifactor provider'+lineno())

        users = Users(self.domain, self.token)
        results = users.delete_multifactor(id=user_id, provider=provider)
        return pretty(results)



    def create_user(self, body):
        if self.debug:
            print('command - create'+lineno())

        users = Users(self.domain, self.token)
        body = json.loads(body)

        # See if the connection is valid
        connection_ids = []
        connections = json.loads(self.get_all_connections())
        for conn in connections:
            print('conn: '+str(conn))
            if 'name' in conn:
                print('found name')
                connection_ids.append(conn['name'])


        if 'connection' in body and body['connection'] not in connection_ids:
            print('The connection id should be : '+str(pretty(connection_ids)))
            sys.exit(1)

        results = users.create(body=body)
        return pretty(results)


    def update_user(self, id, body):
        if self.debug:
            print('command - update user'+lineno())

        users = Users(self.domain, self.token)

        body = json.loads(body)

        # See if the connection is valid
        connection_ids = []
        connections = json.loads(self.get_all_connections())
        for conn in connections:
            print('conn: '+str(conn))
            if 'name' in conn:
                print('found name')
                connection_ids.append(conn['name'])


        if 'connection' in body and body['connection'] not in connection_ids:
            print('The connection id should be : '+str(pretty(connection_ids)))
            sys.exit(1)

        results = users.update(id=id, body=body)
        return pretty(results)

    def get_a_user(self, id, fields, include_fields):
        if self.debug:
            print('command - get_a_user'+lineno())

        users = Users(self.domain, self.token)
        results = users.get(id=id, fields=fields, include_fields=include_fields)
        return pretty(results)

    def unlink_a_user_identity(self, id, provider, user_id ):
        if self.debug:
            print('command - unlink_a_user_identity'+lineno())

        users = Users(self.domain, self.token)
        results = users.unlink_user_account(id=id, provider=provider, user_id=user_id)
        return pretty(results)


    def link_a_user_account(self, id, body):
        if self.debug:
            print('command - link_a_user_account'+lineno())

        users = Users(self.domain, self.token)
        results = users.link_user_account(user_id=id, body=body)
        return pretty(results)

    ##################
    # UserBlocks
    ##################
    def list_user_blocks(self, user_id):
        if self.debug:
            print('command - list_user_blocks'+lineno())

        blocks = UserBlocks(self.domain, self.token)
        return pretty(blocks.get(id=user_id))


    def get_blocks_by_identifier(self, identifier):
        if self.debug:
            print('command - get_blocks_by_identifier'+lineno())

        blocks = UserBlocks(self.domain, self.token)
        return pretty(blocks.get_by_identifier(identifier=identifier))

    def unblock_by_identifier(self, identifier):
        if self.debug:
            print('command - unblock_by_identifier'+lineno())

        blocks = UserBlocks(self.domain, self.token)
        return pretty(blocks.unblock_by_identifier(identifier=identifier))

    def unblock_a_user(self, id):
        if self.debug:
            print('command - unblock_a_user'+lineno())

        blocks = UserBlocks(self.domain, self.token)
        return pretty(blocks.unblock(id=id))


    ##################
    # Users By Email
    ##################

    def user_by_email(self,email):
        if self.debug:
            print('command - user_by_email'+lineno())

        users = UsersByEmail(self.domain, self.token)
        return pretty(users.search_users_by_email(email=email))
