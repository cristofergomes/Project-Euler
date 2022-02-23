# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:02:44 2022

@author: Cris

Project Euler 6
"""
sum_q = 0
q_sum = 0

for i in range(1,101,1):
    sum_q = sum_q + i**2
    q_sum = q_sum + i    
q_sum = q_sum**2
dif = q_sum - sum_q
print(dif)
