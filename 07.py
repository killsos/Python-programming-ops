#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

d = {"name": '魑魅魍魉'}

print d["name"]

d2 = {"age": 23}

d.update(d2)

print(d)

print(type(d.popitem()))

print(d)