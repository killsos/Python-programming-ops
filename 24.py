#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8


temp = 'm24'
func = 'count'

model = __import__(temp)

fn = getattr(model, func)

fn()