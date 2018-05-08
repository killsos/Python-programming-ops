#! /usr/bin/env python

# -*- coding: utf-8 -*-
# coding=utf-8

list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print(index, item)

for index, item in enumerate(list1, 1):
    print(index, item)