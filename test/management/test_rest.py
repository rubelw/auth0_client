import unittest
import sys
import json
import base64
import requests
import mock
from auth0_client.v3.management.rest import RestClient
from auth0_client.v3.exceptions import Auth0Error


class TestRest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}

        mock_get.return_value.text = '["a", "b"]'
        mock_get.return_value.status_code = 200

        response = rc.get('the-url')
        mock_get.assert_called_with('the-url', params=None, headers=headers)

        self.assertEqual(response, ['a', 'b'])

        response = rc.get(url='the/url', params={'A': 'param', 'B': 'param'})
        mock_get.assert_called_with('the/url', params={'A': 'param',
                                                       'B': 'param'},
                                    headers=headers)
        self.assertEqual(response, ['a', 'b'])

        mock_get.return_value.text = ''
        response = rc.get('the/url')
        self.assertEqual(response, '')

    @mock.patch('requests.get')
    def test_get_errors(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_get.return_value.text = '{"statusCode": 999,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'
        mock_get.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.get('the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_post.return_value.text = '{"a": "b"}'

        data = {'some': 'data'}

        mock_post.return_value.status_code = 200
        response = rc.post('the/url', data=data)
        mock_post.assert_called_with('the/url', data=json.dumps(data),
                                     headers=headers)

        self.assertEqual(response, {'a': 'b'})

    @mock.patch('requests.post')
    def test_post_errors(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = '{"statusCode": 999,' \
                                      ' "errorCode": "code",' \
                                      ' "message": "message"}'
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post_errors_with_no_message_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code",
            "error": "error"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'error')

    @mock.patch('requests.post')
    def test_post_errors_with_no_message_or_error_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, '')

    @mock.patch('requests.post')
    def test_post_errors_with_message_and_error_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code",
            "error": "error",
            "message": "message"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post_error_with_code_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"errorCode": "e0",' \
                                          '"message": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_no_error_code(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"message": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_text_response(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = 'there has been a terrible error'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message,
                             'there has been a terrible error')

    @mock.patch('requests.post')
    def test_post_error_with_no_response_text(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = None

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, '')

    @mock.patch('requests.patch')
    def test_patch(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_patch.return_value.text = '["a", "b"]'
        mock_patch.return_value.status_code = 200

        data = {'some': 'data'}

        response = rc.patch(url='the-url', data=data)
        mock_patch.assert_called_with('the-url', data=json.dumps(data),
                                      headers=headers)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.patch')
    def test_patch_errors(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_patch.return_value.text = '{"statusCode": 999,' \
                                       ' "errorCode": "code",' \
                                       ' "message": "message"}'
        mock_patch.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.patch(url='the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.delete')
    def test_delete(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}

        mock_delete.return_value.text = '["a", "b"]'
        mock_delete.return_value.status_code = 200

        response = rc.delete(url='the-url/ID')
        mock_delete.assert_called_with('the-url/ID', headers=headers, params={})

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.delete')
    def test_delete_errors(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_delete.return_value.text = '{"statusCode": 999,' \
                                        ' "errorCode": "code",' \
                                        ' "message": "message"}'
        mock_delete.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.delete(url='the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    def test_disabled_telemetry(self):
        rc = RestClient(jwt='a-token', telemetry=False)
        
        self.assertEqual(rc.base_headers, {})

    def test_enabled_telemetry(self):
        rc = RestClient(jwt='a-token', telemetry=True)

        user_agent = rc.base_headers['User-Agent']
        auth0_client_bytes = base64.b64decode(rc.base_headers['Auth0-Client'])
        auth0_client_json = auth0_client_bytes.decode('utf-8')
        auth0_client = json.loads(auth0_client_json)
        content_type = rc.base_headers['Content-Type']

        from auth0_client import __version__ as auth0_version
        python_version = '{}.{}.{}'.format(sys.version_info.major,
                                           sys.version_info.minor,
                                           sys.version_info.micro)

        client_info = {
            'name': 'auth0-client', 'version': auth0_version,
            'dependencies': [
                {
                    'name': 'requests',
                    'version': requests.__version__
                }
            ],
            'environment': [
                {
                    'name': 'python',
                    'version': python_version
                }
            ]
        }

        self.assertEqual(user_agent, 'Python/{}'.format(python_version))
        self.assertEqual(auth0_client, client_info)
        self.assertEqual(content_type, 'application/json')
