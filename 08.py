#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

d = {"name": '魑魅魍魉'}

d2 = {"age": d}

d3 = d2.copy()

print('d2-age', id(d2['age']))

print('d3-age', id(d3['age']))