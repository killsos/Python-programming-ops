#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import random

# print(random.randint(65, 90))  # 大写字母
#
# print(chr(random.randint(65, 90)))  # 大写字母


def makeRandomcharAndnumber():
    code = []
    for i in  range(6):
        if i == random.randint(1,5):
            code.append(str(random.randint(1,5)))
        else:
            code.append(chr(random.randint(65, 90)))
    return ''.join(code)

print(makeRandomcharAndnumber())