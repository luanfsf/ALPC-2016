#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

dimensao = 0

while dimensao < 1 or dimensao > 25 :
    print "Digite a dimensão da matrix, de 1 a 25"
    dimensao = int(input())

matrix = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print "- - -",
    print ("-")
    for coluna in range(dimensao):
        print "|%4d" %matrix[linha][coluna],
    
    print "|",
    print ""
for i in range(dimensao):
    print "- - -",
print ("-")
# bastante ineficiente
for linha in range(dimensao):
    for coluna in range(dimensao):
        for i in range(dimensao):
            for j in range(dimensao):
                if matrix[linha][coluna] < matrix[i][j]:
                    aux = matrix[linha][coluna]
                    matrix[linha][coluna] = matrix[i][j]
                    matrix[i][j] = aux

print "Ordenado com bubble sort"

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print "- - -",
    print ("-")
    for coluna in range(dimensao):
        print "|%4d" %matrix[linha][coluna],
    
    print "|",
    print ""
for i in range(dimensao):
    print "- - -",
print ("-")
