from __future__ import division, print_function, absolute_import, unicode_literals


class AwsCliMenuError(Exception):
    """Base class of application specific exceptions"""


class EncodingError(AwsCliMenuError):
    """Encode error."""


class SettingError(AwsCliMenuError):
    """Setting error."""


class ConfigError(AwsCliMenuError):
    """Configuration error."""

    def __init__(self, path, msg=''):
        AwsCliMenuError.__init__(self, '%s: %s' % (path, msg))
