#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

def multi(matrix, fator):
  return fator * matrix

dimensao = 0

while dimensao < 1 or dimensao > 12 :
    print "Digite a dimensão da matrix, de 1 a 12"
    dimensao = int(input())

matrix = [[random.randrange(1, 999, 1) for i in range(dimensao)] for j in range(dimensao)]

for linha in range(dimensao): # Exibe a grade da matrix
  for i in range(dimensao):
      print "-----",
  print ("-")
  for coluna in range(dimensao):
    print "|%4d" %matrix[linha][coluna],
    
  print "|",
  print ""
  
fator = 0
atual = 0
print "Digite um número para multiplicar essa matriz entre 1 e 10"
while fator < 1 or fator > 10 :
    print "Digite a dimensão da matrix, de 1 a 12"
    fator = int(input())

for linha in range(dimensao): # Exibe a grade da matrix
  for i in range(dimensao):
      print "-----",
  print ("-")
  for coluna in range(dimensao):
    atual = matrix[linha][coluna]
    print "|%4d" %multi(atual, fator),
    
  print "|",
  print ""
for i in range(dimensao):
      print "-----",
print ("-")