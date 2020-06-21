#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:09:01 2020

@author: priya
"""

number=[10,20,0,5,0,30]
for n in number:
    if n==0:
        print("not able to devide by zero")
        continue
    print("100/{}".format(n,100/n))