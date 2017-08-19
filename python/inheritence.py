# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class People(object):
    def eat(self):
        print("people eat")


class Man(People):
    def eat(self):
        print("man eat")


class Woman(People):
    def eat(self):
        super(Woman, self).eat()
        print("woman eat")


People().eat()
Man().eat()
Woman().eat()
