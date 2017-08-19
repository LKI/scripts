# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def wrap(x):
    print("wrapping {}".format(x))
    return x


print("calculating a")
a = {"a": wrap(42), "b": "universe"}.get("b")
print("a is {}".format(a))

print("calculating b")
b = {"a": lambda x: wrap(42), "b": lambda: "universe"}.get("b")()  # lazy
print("b is {}".format(b))
