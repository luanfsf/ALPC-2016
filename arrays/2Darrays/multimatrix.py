#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

def multi(matrix, fator):
  return fator * matrix

dimencao = 0

while dimencao < 1 or dimencao > 12 :
    print "Digite a dimencao da matrix, de 1 a 12"
    dimencao = int(input())

matrix = [[random.randrange(1, 999, 1) for i in range(dimencao)] for j in range(dimencao)]

for linha in range(dimencao): # Exibe a grade da matrix
  for i in range(dimencao):
      print "-----",
  print ("-")
  for coluna in range(dimencao):
    print "|%4d" %matrix[linha][coluna],
    
  print "|",
  print ""
  
fator = 0
atual = 0
print "Digite um numero para multiplicar essa matriz entre 1 e 10"
while fator < 1 or fator > 10 :
    print "Digite a dimencao da matrix, de 1 a 12"
    fator = int(input())

for linha in range(dimencao): # Exibe a grade da matrix
  for i in range(dimencao):
      print "-----",
  print ("-")
  for coluna in range(dimencao):
    atual = matrix[linha][coluna]
    print "|%4d" %multi(atual, fator),
    
  print "|",
  print ""
for i in range(dimencao):
      print "-----",
print ("-")