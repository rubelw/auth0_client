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
    @patch('auth0_client.v3.management.custom_domains.CustomDomains.get_all')
    def test_get_all_connections(self, domains, exit):
        domains.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        real_results = client.get_custom_domains()

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.custom_domains.CustomDomains.create_new')
    def test_configure_new_custom_domain(self, domains, exit):
        domains.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'


        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.create_new_custom_domain(body=body)


        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.custom_domains.CustomDomains.get_domain_by_id')
    def test_get_custom_domain_configuration(self, domains, exit):
        domains.return_value = '123'

        debug = False
        exit.return_value = None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client = class_to_test(config_dict)

        real_results = client.get_custom_domain(id='123')

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.custom_domains.CustomDomains.delete')
    def test_delete_custom_domain_configuration(self, domains, exit):
        domains.return_value = '123'

        debug = False
        exit.return_value = None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client = class_to_test(config_dict)

        real_results = client.delete_custom_domain(id='123')

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0_client.v3.management.custom_domains.CustomDomains.verify')
    def test_verify_a_custom_domain(self, domains, exit):
        domains.return_value = '123'

        debug = False
        exit.return_value = None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client = class_to_test(config_dict)

        real_results = client.verify_custom_domain(id='123')

        self.assertEqual('"123"', real_results)


