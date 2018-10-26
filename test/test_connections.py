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


class TestBlacklist(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0.v3.management.connections.Connections.all')
    def test_get_all_connections(self, connections, exit):
        connections.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.get_all_connections()


        self.assertEqual('[\n\t"1",\n\t"2",\n\t"3"\n]', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.connections.Connections.get')
    def test_get_a_connection(self, connections, exit):
        connections.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.get_a_connection(id='123', fields='456', include_fields='789')


        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.connections.Connections.delete_user_by_email')
    def test_delete_a_connection_user(self, connections, exit):
        connections.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.delete_a_connection_user(id='123', email='123')


        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.connections.Connections.update')
    def test_update_a_connection(self, connections, exit):
        connections.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.update_a_connection(id='123', body=body)


        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.connections.Connections.delete')
    def test_delete_a_connection_user(self, connections, exit):
        connections.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.delete_a_connection(id='123')


        self.assertEqual('"123"', real_results)
