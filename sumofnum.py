#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:10:55 2020

@author: priya
"""

#find sum of first n number
n=int(input("enter some number"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1

print("sum is",sum)