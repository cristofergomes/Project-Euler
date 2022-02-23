# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:08:34 2022

@author: Cris

Project Euler 7
"""
count = 1
for i in range(3,300000000,1):
    for j in range(2,i,1):
        sobra = i%j
        if sobra == 0:
            break
    if sobra != 0  and j >= i/2:
        count = count + 1
    if count == 10001:
        print(i)
        break
