#!/usr/bin/env python

'''1) Faca um programa que receba a quantidade de pecas
vendidas por vendedor e armazene essas quantidades em um
vetor. 

Receba tambem o preco da peca vendida de cada
vendedor e armazene esses precos em outro vetor.

Existem apenas dez vendedores e cada vendedor pode vender apenas
um tipo de peca, isto e, para cada vendedor existe
apenas um preco.

Calcule e mostre a quantidade total de pecas vendidas por todos os 
vendedores e para cada vendedor calcule e mostre o valor total da
venda, isto e, a quantidade de pecas * o preco da peca.'''

'''
w, h = 8, 5. 
Matrix = [[0 for x in range(w)] for y in range(h)] 
vendedores = [0][0]
'''

for v in range (0,10):
  
  print "Digite a quantidade de pecas vendidas"
  npecas = int(input())
  vetpecas = [0] * npecas
  
  for i in range(npecas):
    vetpecas[i] = int(input())
  print "digite o valor da peca"
  
  vpeca = float(input())


print vetpecas