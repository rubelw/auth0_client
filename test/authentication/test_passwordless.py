import unittest
import mock
from auth0_client.v3.authentication.passwordless import Passwordless


class TestPasswordless(unittest.TestCase):

    @mock.patch('auth0_client.v3.authentication.passwordless.Passwordless.post')
    def test_email(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email(client_id='cid',
                email='a@b.com',
                send='snd',
                auth_params={'a': 'b'})

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'email': 'a@b.com',
            'send': 'snd',
            'authParams': {'a': 'b'},
            'connection': 'email',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0_client.v3.authentication.passwordless.Passwordless.post')
    def test_sms(self, mock_post):
        p = Passwordless('my.domain.com')

        p.sms(client_id='cid', phone_number='123456')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'phone_number': '123456',
            'connection': 'sms',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0_client.v3.authentication.passwordless.Passwordless.post')
    def test_sms_login(self, mock_post):

        p = Passwordless('my.domain.com')

        p.sms_login(client_id='cid', phone_number='123456', code='abcd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'sms',
            'grant_type': 'password',
            'username': '123456',
            'password': 'abcd',
            'scope': 'openid',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0_client.v3.authentication.passwordless.Passwordless.post')
    def test_sms_login_with_scope(self, mock_post):

        p = Passwordless('my.domain.com')

        p.sms_login(client_id='cid', phone_number='123456',
                    code='abcd', scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'sms',
            'grant_type': 'password',
            'username': '123456',
            'password': 'abcd',
            'scope': 'openid profile',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })