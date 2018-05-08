#! /usr/bin/env python

# -*- coding: utf-8 -*-
# coding=utf-8

def foo(*args):
    print(args)
    print(type(args))
    for item in args:
        print(item)

def bar(**args):
    print(args)
    print(type(args))
    for item in args:
        print(item, ':', args[item])


foo(123, 345, 'foo')


bar(name='person', age=12)

user = {'name': 'user', 'age': 18}    # 调用方式

bar(**user)