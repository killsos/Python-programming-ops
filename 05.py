#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

f = file('/etc/passwd')

for line in f.readlines():
  print line.strip('\n')
    