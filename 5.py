# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:58:32 2022

@author: Cris

Project Euler 5
"""

for i in range(2520,30000000000,1):
    for j in range(1,21,1):
        resto = i%j
        if resto != 0:
            break
    if j == 20 and resto == 0:
        print(i)
        break
print("parou")