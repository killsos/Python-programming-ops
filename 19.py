#! /usr/bin/env python

# -*- coding: utf-8 -*-
# coding=utf-8

def MreadLines():
    seek = 0
    while True:
        with open('gen.txt') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return


for item in MreadLines():
    print(item)