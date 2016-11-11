#!/usr/bin/env python
# encoding: utf-8
# python 3.5
import random

def multi(matrix, fator):
  return fator * matrix

dimensao = 0

while dimensao < 1 or dimensao > 12 :
    print ("Digite a dimensão da matrix, de 1 a 12")
    dimensao = int(input())

matrix = [[random.randrange(1, 999, 1) for i in range(dimensao)] for j in range(dimensao)]

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print ("- - -", end=" ")
    print ("-")
    for coluna in range(dimensao):
        print ("|%4d " %matrix[linha][coluna], end="")
    
    print ("|", end="")
    print ("")
for i in range(dimensao):
    print ("- - -", end=" ")
print ("-")
fator = 0
atual = 0
print ("Digite um número para multiplicar entre 1 e 10")
while fator < 1 or fator > 10 :
    fator = int(input())

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print ("- - -", end=" ")
    print ("-")
    for coluna in range(dimensao):
        atual = matrix[linha][coluna]
        print ("|%4d " %multi(atual, fator), end="")
    
    print ("|", end="")
    print ("")
for i in range(dimensao):
    print ("- - -", end=" ")
print ("-")