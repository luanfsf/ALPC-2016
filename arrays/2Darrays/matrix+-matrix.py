#!/usr/bin/env python
# encoding: utf-8
# python 3.5
import random

# gerar duas matrizes NxN e perguntar
# se deseja somar ou diminuir a primeira pela segunda

dimensao = 0

while dimensao < 1 or dimensao > 10 :
    print ("Digite a dimensão das matrizes, de 1 a 10 :", end="")
    dimensao = int(input())

matrix1 = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]
matrix2 = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]
resultado = [[0] * dimensao for i in range(dimensao)]

for linha in range(dimensao): # Exibe a grade da matrix
    for coluna in range(dimensao):
        print ("|%5d" %matrix1[linha][coluna], end="")
    print ("| + - ", end="")
    for coluna in range(dimensao):
        print ("|%5d" %matrix2[linha][coluna], end="")
    print ("|", end="")
    print ("")

opcao = 0
while opcao <1 or opcao > 2:
    print ("Se deseja somar as matrizes digite 1\nSe deseja diminuir digite 2")
    opcao = int(input())

if opcao == 1:
    for i in range(dimensao):
        for j in range(dimensao):
            resultado[i][j] = matrix1[i][j] + matrix2[i][j]

if opcao == 2:
    for i in range(dimensao):
        for j in range(dimensao):
            resultado[i][j] = matrix1[i][j] - matrix2[i][j]
            
print ("Resultado")
for linha in range(dimensao): # Exibe a grade da matrix
    for coluna in range(dimensao):
        print ("| %5d" %resultado[linha][coluna], end="")
    print ("|", end="")
    print ("")