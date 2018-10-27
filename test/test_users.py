import json
import sys
import unittest
from contextlib import contextmanager
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from mock import patch

from auth0_client.Auth0Client import Auth0Client as class_to_test

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestUsers(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.list')
    def test_list_or_search_users(self, users, exit):
        users.return_value={'total':1}


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.list_users(
        )

        self.assertEqual('[\n]', real_results)

    @patch('auth0_client.v3.management.connections.Connections.all')
    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.create')
    def test_create_a_user(self, users, exit, connections):
        users.return_value='123'
        connections.return_value=json.loads('[{"name": "My connection","options": {},"id": "con_0000000000000001","strategy": "auth0","realms": [  ""],"is_domain_connection": false,"metadata": {}}]')


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)
        body='{"123":"xxx"}'

        real_results = client.create_user(
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.get')
    def test_get_a_user(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_a_user(
            id='123',
            fields=['123'],
            include_fields=True
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.delete')
    def test_delete_a_user(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.delete_user(
            user_id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('auth0_client.v3.management.connections.Connections.all')
    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.update')
    def test_update_a_user(self, users, exit, connections):
        users.return_value='123'
        connections.return_value=json.loads('[{"name": "My connection","options": {},"id": "con_0000000000000001","strategy": "auth0","realms": [  ""],"is_domain_connection": false,"metadata": {}}]')

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)
        body='{"123":"xxx"}'

        real_results = client.update_user(
            id='123',
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.get_guardian_enrollments')
    def test_get_a_list_of_guardian_enrollments(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_list_of_guardian_enrollments(
            user_id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.get_log_events')
    def test_get_users_log_events(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_user_log_events(
            user_id='123'
        )

        self.assertEqual('[\n\t"1",\n\t"2",\n\t"3"\n]', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.delete_multifactor')
    def test_delete_a_users_multifactor_provider(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.delete_a_users_multifactor_provider(
            user_id='123',
            provider='123'
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.unlink_user_account')
    def test_unlink_a_user_identity(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.unlink_a_user_identity(
            user_id='123',
            provider='123',
            id='abc'
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.regenerate_recovery_code')
    def test_generate_new_guardian_recovery_code(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.generate_new_user_guardian_recovery_code(
            user_id='123'
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0_client.v3.management.users.Users.link_user_account')
    def test_link_a_user_account(self, users, exit):
        users.return_value='123'

        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)
        body='{"123":"xxx"}'

        real_results = client.link_a_user_account(
            id='123',
            body= body
        )

        self.assertEqual('"123"', real_results)



