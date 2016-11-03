#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random
dimensao = 0

while dimensao < 1 or dimensao > 25 :
    print "Digite a dimensão da matrix, de 1 a 25 :",
    dimensao = int(input())

matrix = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]

print "Uma matriz %dx%d foi criada com numeros aleatórios"  %(dimensao, dimensao)
print "\033[92mNumeros dessa cor são pares!"
print "\033[91mNumeros dessa cor são ímpares!"

par = 0
impar = 0

for linha in range(dimensao): # Exibe a grade da matrix
    for i in range(dimensao):
        print "\033[94m- - -",
    print ("-")
    for coluna in range(dimensao):
        if matrix[linha][coluna] % 2 == 0:
            par += 1
            print "|\033[92m%4d\033[94m" %matrix[linha][coluna],
        else:
            print "|\033[91m%4d\033[94m" %matrix[linha][coluna],
            impar += 1
    
    print "|",
    print ""
for i in range(dimensao):
    print "\033[94m- - -",
print ("-")