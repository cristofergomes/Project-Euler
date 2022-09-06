# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:46:13 2022

@author: Cris

Project Euler 10
"""
soma = 2
for i in range(3,2000000,2): #tirando 2, todo numero par não é primo
    for j in range(2,i,1):
        sobra = i%j
        if sobra == 0:
            break
            
# Quando você faz uma divisão x/y = z, automaticamente vc obtem a resposta de x/z que é y.
# Então, no somatório em y de x/y=z, quando o y for maior que z e nenhum z é inteiro, significa que (em um x/z = y) não há nenhum z inteiro que dá um y inteiro.

        if j > (i/j):
            break
    if sobra != 0  and j > (i/j):
        soma = soma+i
print("acabou")
print(soma)
