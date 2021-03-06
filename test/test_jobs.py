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


class TestJobs(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.get')
    def test_get_a_job(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_a_job(
            id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.get_failed_job')
    def test_get_failed_job_error_details(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_failed_job_error_details(
            id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.get_job_results')
    def test_get_results_of_a_job(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_results_of_a_job(
            id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.export_users')
    def test_create_job_to_export_users(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        body= '{"123":"xxx"}'
        real_results = client.create_job_to_export_users(
            body=body
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.import_users')
    def test_create_job_to_import_users(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.create_job_to_import_users(
            connection_id='122',
            file_obj='test',
            upsert=True

        )

        self.assertEqual('"123"', real_results)


    @patch('sys.exit')
    @patch('auth0_client.v3.management.jobs.Jobs.send_verification_email')
    def test_send_a_verify_email_address_email(self, jobs, exit):
        jobs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)
        body= '{"123":"xxx"}'
        real_results = client.send_a_verify_email_address_email(
            body=body

        )

        self.assertEqual('"123"', real_results)


