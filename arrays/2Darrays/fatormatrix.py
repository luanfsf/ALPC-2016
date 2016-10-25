#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random
dimensao = 0

while dimensao < 1 or dimensao > 5 :
    print "Digite a dimensão da matrix, de 1 a 5"
    dimensao = int(input())
    
matrix = [[random.randrange(1, 999, 1) for i in range(dimensao)] for j in range(dimensao)]

for linha in range(dimensao): # Exibe a grade da matrix
  for i in range(dimensao):
      print "- - -",
  print "-"
  for coluna in range(dimensao):
    print "|%4d" %matrix[linha][coluna],
    
  print "|",
  print ""
for i in range(dimensao):
    print "- - -",
print "-"

fator = 0
atual = 0
print "Digite um número para redimensionar essa matriz entre 2 e 5"
while fator < 2 or fator > 5 :
    fator = int(input())
    
novamatrix = [[0] * (dimensao * fator) for i in range(dimensao * fator)]
    
for linha in range(dimensao * fator): # Exibe a grade da matrix
    for i in range(dimensao * fator):
        print "- - -",
    print "-"
    
    for coluna in range(dimensao * fator):
        # o bloco [i][j] deve ser escrito N * em linha e coluna
        novamatrix[linha][coluna] = 0
        print "|%4d" %novamatrix[linha][coluna],
    
    print "|",
    print ""
for i in range(dimensao*  fator):
    print "- - -",
print "-"