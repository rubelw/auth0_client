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


class TestGuardian(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.all_factors')
    def test_get_a_list_of_factors_and_statuses(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.list_factors(
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.get_enrollment')
    def test_get_a_guardian_enrollment(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_a_guardian_enrollment(
            id='123'
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.delete_enrollment')
    def test_delete_a_guardian_enrollment(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.delete_a_guardian_enrollment(
            id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.get_templates')
    def test_get_enrollment_and_verification_templates(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.list_enrollment_templates(
        )

        self.assertEqual('"123"', real_results)



    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.update_templates')
    def test_update_enrollment_and_verification_templates(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.update_enrollment_and_verification_templates(
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.get_factor_providers')
    def test_get_guardian_sns_factor_provider_configuration(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.list_sns_factor_provider_config(
        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.get_factor_providers')
    def test_get_guardian_twilio_factor_provider_configuration(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.list_twilio_factor_provider_config(
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.update_factor_providers')
    def test_update_guardians_twilio_sms_factor_provider(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.update_guardians_twilio_sms_factor_provider(
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.create_enrollment_ticket')
    def test_create_a_guardian_enrollment_ticket(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.create_a_guardian_enrollment_ticket(
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0.v3.management.guardian.Guardian.update_factor_providers')
    def test_update_guardian_factor(self, guardian, exit):
        guardian.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.update_guardian_factor(
            name='abc',
            body=body
        )

        self.assertEqual('"123"', real_results)



