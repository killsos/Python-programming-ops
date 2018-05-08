#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import hashlib

hash = hashlib.md5()

hash.update('admin'.encode('utf-8'))

print(hash.hexdigest())