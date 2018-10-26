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


class TestTenants(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0.v3.management.tenants.Tenants.get')
    def test_get_tenant_settings(self, stats, exit):
        stats.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_tenants(
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.tenants.Tenants.update')
    def test_update_tenant_settings(self, stats, exit):
        stats.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)
        body='{"123":"xxx"}'
        real_results = client.update_tenant_settings(
            body=body
        )

        self.assertEqual('"123"', real_results)

