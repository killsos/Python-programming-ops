# -*- coding: utf-8 -*-
# coding=utf-8

f = file('README.md', 'r')

for line in f.readlines():
  line = line.strip('\n')
  print line    