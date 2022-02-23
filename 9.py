# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:28:34 2022

@author: Cris

Project Euler 9
"""

for a in range(3,10000,1):
    for b in range(a+1,10000,1):
        c_q = a**2 + b**2
        c = c_q**(1/2)
        if c%1 == 0:
            c = int(c)
            soma = a + b + c
        if soma == 1000:
            break
    if soma == 1000:
        prod = a*b*c
        print(prod)
        break