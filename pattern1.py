#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:20:36 2020

@author: priya
"""

n=int(input("enter number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()