from __future__ import division, print_function, absolute_import, unicode_literals
import inspect


DEBUG=0


#
# functions for handling optional values
#
def omap(function, optional):
    """Map optional value"""

    if (DEBUG):
        print('commons.functional.py - omap(function,optional)- called by:'+str(inspect.stack()[1][3]))

    return None if optional is None else function(optional)


def oget(optional, default=None):
    """Get optional value or default value"""

    if (DEBUG):
        print('commons.functional.py - oget(optinal,default=None)- called by:'+str(inspect.stack()[1][3]))

    return default if optional is None else optional


def ozip(*optionals):
    """Zip optional values. Return None if one value or the other is None."""

    if (DEBUG):
        print('commons.functional.py - ozip(*optionals)- called by:'+str(inspect.stack()[1][3]))

    return None if any(x is None for x in optionals) else tuple(optionals)
