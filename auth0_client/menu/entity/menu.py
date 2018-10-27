from __future__ import division, print_function, absolute_import, unicode_literals

import six
from auth0_client.menu.commons.string import to_unicode
from auth0_client.menu.commons.collection import get_single_item
from auth0_client.menu.commons.types import *
from auth0_client.menu.entity import Meta, Item
import inspect


DEBUG=1


class Menu(Item):
    """
    Menu is built from an one-element dict having title string as key and item list element as value
    """

    @types(title=Unicode, items=ListOf(Item), meta=Meta)
    def __init__(self, title, items, meta=Meta()):
        """
        :param title:
        :param items:
        :param meta:
        :return:
        """
        if (DEBUG):
            print('entity.menu.py - Menu - __init__(self,title,items,meta)- caller:'+str(inspect.stack()[1][3]))

        Item.__init__(self, ('title', title), ('items', items), ('meta', meta))

    @staticmethod
    @types(Item, data=dict, meta=Meta)
    def parse(data, meta, loader, encoding='utf-8', depth=0):
        """
        :param data:
        :param meta:
        :param loader:
        :param encoding:
        :param depth:
        :return:
        """
        if (DEBUG):
            print('entity.menu.py - Menu - parse()- caller:'+str(inspect.stack()[1][3]))

        from auth0_client.menu.entity import KEYWORD_META, Item

        if (DEBUG):
            print('read meta configurations')
            print(data)

        if KEYWORD_META in data:
            meta = meta.updated(data[KEYWORD_META], encoding)
            del data[KEYWORD_META]

        assert len(data) == 1, 'Menu should have only one item, not %s.' % len(data)

        title, content = get_single_item(data)
        assert isinstance(title, six.string_types), 'Menu title must be string, not %s.' % type(title).__name__
        assert isinstance(content, list), 'Menu content must be list, not %s.' % type(content).__name__
        title = to_unicode(title, encoding)

        items = [Item.parse(item, meta, loader, encoding, depth + 1) for item in content]
        return Menu(title, items, meta)

    @types(Unicode)
    def formatted(self):
        """Return formatted string for pretty printing."""
        if (DEBUG):
            print('entity.menu.py - Menu - formatted()- caller:'+str(inspect.stack()[1][3]))

        return '\n'.join(
            ['# %s:' % self.title] + ['  %s' % line for x in self.items for line in x.formatted().splitlines()])
