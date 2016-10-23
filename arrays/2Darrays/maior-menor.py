#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random
dimensao = 0

while dimensao < 1 or dimensao > 25 :
    print "Digite a dimensão da matrix, de 1 a 25 :",
    dimensao = int(input())

matrix = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]


maior = 0
menor = 0

for linha in range(dimensao):
    for coluna in range(dimensao):
        if (linha == 0) and (coluna == 0):
            menor = matrix[linha][coluna]
        elif matrix[linha][coluna] < menor:
            menor = matrix[linha][coluna]
        elif matrix[linha][coluna] > maior:
            maior = matrix[linha][coluna]


print "Uma matriz %dx%d foi criada com numeros aleatórios \nE o maior é %4d e o menor é %3d" %(dimensao, dimensao, maior, menor)

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print "\033[94m- - -",
    print ("-")
    for coluna in range(dimensao):
        if matrix[linha][coluna] == maior:
            print "|\033[92m%4d\033[94m" %matrix[linha][coluna],
        elif matrix[linha][coluna] == menor:
            print "|\033[91m%4d\033[94m" %matrix[linha][coluna],
        else:
            print "\033[94m|%4d" %matrix[linha][coluna],
    
    print "|",
    print ""
for i in range(dimensao):
    print "\033[94m- - -",
print ("-")

