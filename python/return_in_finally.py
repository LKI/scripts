# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def return_in_finally():
    try:
        return True
    finally:
        return False


print(return_in_finally())
