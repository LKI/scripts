# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def f(default_list=[], default_tuple=(), default_dict={}):
    print(default_list, default_tuple, default_dict)
    default_list.append(1)
    default_tuple = (1,)
    default_dict[2] = [2]


f()
f()
