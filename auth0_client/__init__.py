from __future__ import absolute_import, division, print_function
from auth0_client.Auth0Client import Auth0Client #noqa

try:
    from auth0_client._build import __build__
except ImportError:
    pass
else:
    __version__ = '{}.{}'.format(__version__, __build__)

__all__ = [
]
__title__ = 'auth0_client'
__version__ = '0.6.1'
__author__ = 'Will Rubel'
__author_email__ = 'willrubel@gmail.com'