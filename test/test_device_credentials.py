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


class TestDeviceCredentials(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0.v3.management.device_credentials.DeviceCredentials.get')
    def test_list_device_credentials(self, device, exit):
        device.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_device_credentials(
            user_id='123',
            client_id='456',
            cred_type='abc',
            fields='email',
            include_fields=True
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.device_credentials.DeviceCredentials.create')
    def test_create_a_device_public_key(self, device, exit):
        device.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.create_device_public_key(
            body=body
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.device_credentials.DeviceCredentials.delete')
    def test_delete_a_device_credential(self, device, exit):
        device.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.delete_device_credentials(
            id='123'
        )

        self.assertEqual('"123"', real_results)


