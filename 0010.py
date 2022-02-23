# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:46:13 2022

@author: Cris

Project Euler 10
"""
soma = 2
for i in range(3,2000000,2): #tirando 2, todo numero par n é primo
    for j in range(2,i,1):
        sobra = i%j
        if sobra == 0:
            break
# A lógica que eu usei para a otimização foi a seguinte
# Se você faz uma divisão x/y e obtem z, automaticamente vc obtem a resposta de x/z que é y
# Então se o y for maior que x/y, então vc ja testou todas divisões para x 
        if j > (i/j):
            break
    if sobra != 0  and j > (i/j):
        soma = soma+i
print("acabou")
print(soma)
