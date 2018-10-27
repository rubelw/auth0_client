from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from auth0_client.menu.commons.string import is_unicode, to_bytes, to_unicode
import inspect

DEBUG=0

def print_safe(str_or_bytes, encoding='utf-8', errors='ignore', output=sys.stdout, newline='\n'):
    """
    Print unicode or bytes universally.

    :param str_or_bytes: string
    :param encoding: encoding
    :param output: output file handler
    :param errors: error handling scheme. Refer to codecs.register_error.
    """

    if (DEBUG):
        print('commons.io.py - print_safe(str_or_bytes,encoding=utf-8,errors=ignore,output-sys.stdout,newline=\n)- called by:'+str(inspect.stack()[1][3]))

    writer = output.buffer if hasattr(output, 'buffer') else output

    # When the input type is bytes, verify it can be decoded with the specified encoding.
    decoded = str_or_bytes if is_unicode(str_or_bytes) else to_unicode(str_or_bytes, encoding, errors)
    encoded = to_bytes(decoded, encoding, errors)

    writer.write(encoded + to_bytes(newline, encoding, errors))
    output.flush()
