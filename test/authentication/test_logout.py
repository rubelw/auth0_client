import unittest
import mock
from auth0_client.v3.authentication.logout import Logout


class TestLogout(unittest.TestCase):

    @mock.patch('auth0_client.v3.authentication.logout.Logout.get')
    def test_logout(self, mock_get):

        g = Logout('my.domain.com')

        g.logout(client_id='cid',
                 return_to='rto')

        args, kwargs = mock_get.call_args

        self.assertEqual(args[0], 'https://my.domain.com/v2/logout?client_id=cid&returnTo=rto')
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0_client.v3.authentication.logout.Logout.get')
    def test_federated_logout(self, mock_get):

        g = Logout('my.domain.com')

        g.logout(client_id='cid',
                 return_to='rto',
                 federated=True)

        args, kwargs = mock_get.call_args

        self.assertEqual(args[0], 'https://my.domain.com/v2/logout?federated&client_id=cid&returnTo=rto')
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })
