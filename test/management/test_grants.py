import unittest
import mock
from auth0_client.v3.management.grants import Grants


class TestGrants(unittest.TestCase):

    @mock.patch('auth0_client.v3.management.grants.RestClient')
    def test_get_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Grants(domain='domain', token='jwttoken')
        g.get_all(user_id='an-id',client_id='an-id',audience='test')

        args, kwargs = mock_instance.get.call_args


        mock_instance.get.assert_called_with(
            'https://domain/api/v2/grants', params={'user_id': 'an-id', 'client_id': 'an-id', 'audience': 'test', 'page': None, 'per_page': None, 'include_totals': 'false'}
        )


    @mock.patch('auth0_client.v3.management.grants.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Grants(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/grants/an-id'
        )
