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
    @patch('auth0.v3.management.client_grants.ClientGrants.all')
    def test_get_all_client_grants(self, grants, exit):
        grants.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.get_client_grants()


        self.assertEqual("['1', '2', '3']", str(json.loads(real_results)))

    @patch('sys.exit')
    @patch('auth0.v3.management.client_grants.ClientGrants.create')
    def test_create_a_client_grant(self, grants, exit):
        grants.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.create_client_grant(body=body)


        self.assertEqual('123', str(json.loads(real_results)))

    @patch('sys.exit')
    @patch('auth0.v3.management.client_grants.ClientGrants.delete')
    def test_delete_a_client_grant(self, grants, exit):
        grants.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.delete_client_grant(id='123')


        self.assertEqual('123', str(json.loads(real_results)))

    @patch('sys.exit')
    @patch('auth0.v3.management.client_grants.ClientGrants.update')
    def test_update_a_client_grant(self, grants, exit):
        grants.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.update_client_grant(id='123', body=body)


        self.assertEqual('123', str(json.loads(real_results)))


