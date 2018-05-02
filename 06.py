#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

f = file('test1.txt', 'w')

f.write('魑魅魍魉')

print f.isatty()

f.close();