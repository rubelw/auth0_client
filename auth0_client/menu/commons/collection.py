from __future__ import division, print_function, absolute_import, unicode_literals

import six
import inspect

__all__ = ['get_single_item', 'get_single_key', 'get_single_value', 'distinct']

DEBUG=0

def get_single_item(d):
    """Get an item from a dict which contains just one item."""

    if (DEBUG):
        print('commons.collection.py - get_single_item(d)- called by:'+str(inspect.stack()[1][3]))
        print('Get an item from a dict which contains just one item')

    assert len(d) == 1, 'Single-item dict must have just one item, not %d.' % len(d)
    return next(six.iteritems(d))


def get_single_key(d):
    """Get a key from a dict which contains just one item."""

    if (DEBUG):
        print('commons.collection.py - get_single_key(d)- called by:'+str(inspect.stack()[1][3]))
        print('Get a key from a dict which contains just one item')

    assert len(d) == 1, 'Single-item dict must have just one item, not %d.' % len(d)
    return next(six.iterkeys(d))


def get_single_value(d):
    """Get a value from a dict which contains just one item."""

    if (DEBUG):
        print('commons.collection.py - get_single_value(d)- called by:'+str(inspect.stack()[1][3]))
        print('Get a value from a dict which contains just one item')

    assert len(d) == 1, 'Single-item dict must have just one item, not %d.' % len(d)
    return next(six.itervalues(d))


def distinct(xs):
    """Get the list of distinct values with preserving order."""
    # don't use collections.OrderedDict because we do support Python 2.6

    if (DEBUG):
        print('commons.collection.py - distinct(xs)- called by:'+str(inspect.stack()[1][3]))
        print('Get the list of distinct values from preserving order')

    seen = set()
    return [x for x in xs if x not in seen and not seen.add(x)]
