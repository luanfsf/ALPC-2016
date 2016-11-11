#!/usr/bin/env python
# encoding: utf-8
# python 3.5
import random
dimensao = 0

while dimensao < 1 or dimensao > 20 :
    print ("Digite a dimensão da matrix, de 1 a 20 :", end="")
    dimensao = int(input())

somalinha = [0] * dimensao
somacoluna = [0] * dimensao

matrix = [[random.randrange(1, 9999, 1) for i in range(dimensao)] for j in range(dimensao)]

print ("Uma matriz %dx%d foi criada com numeros aleatórios.\nAs somas das respectivas linhas estão à direita e \nas das colunas estão sob as colunas.(\033[91mvermelho\033[0m)"  %(dimensao, dimensao) )

for linha in range(dimensao):
    for coluna in range(dimensao):
        somalinha[linha] += matrix[linha][coluna]
        somacoluna[coluna] += matrix[linha][coluna]

for linha in range(dimensao): # Exibe a grade da matrix
    for coluna in range(dimensao):
        print ("\033[94m| \033[92m%4d \033[94m" %matrix[linha][coluna], end="")
    print ("| \033[91m%6d\033[94m" %(somalinha[linha]), end="" )
    print ("|",end="")
    print ("")
for i in range(dimensao):
    print ("|\033[91m%6d\033[94m" %(somacoluna[i]), end="")
print ("|")