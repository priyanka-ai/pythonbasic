#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:31:11 2020

@author: priya
"""

n=int(input("enter number of rows"))
for i in range(n+1,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()