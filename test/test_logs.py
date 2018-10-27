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


class TestLogs(unittest.TestCase):
    """
    Test command class
    """
    @patch('sys.exit')
    @patch('auth0_client.v3.management.logs.Logs.get')
    def test_get_log_event_by_id(self, logs, exit):
        logs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.get_log_events_by_id(
            id='123'
        )

        self.assertEqual('"123"', real_results)

    @patch('sys.exit')
    @patch('auth0_client.v3.management.logs.Logs.search')
    def test_search_log_events(self, logs, exit):
        logs.return_value='123'


        debug = False
        exit.return_value=None
        config_dict = {}
        config_dict['debug'] = debug
        config_dict['domain'] = 'test'
        config_dict['client_id'] = 'id'
        config_dict['client_secret'] = 'secret'

        client= class_to_test(config_dict)

        real_results = client.search_log_events(
            page=0,
            per_page=2,
            sort='test',
            fields='test',
            include_fields=True,
            include_totals=True,
            from_id='test',
            take='test',
            query='test'
        )

        self.assertEqual('"123"', real_results)


