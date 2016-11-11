#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random
vetor = [random.randrange(1,999, 1) for i in range(20)]
array = [[0] * 5 for i in range(4)]

varce = [0] * 5
varbe = [0] * 4

proximo = 0
total = 0
total2 = 0
totvarbe = 0
totvarce = 0

for i in range(4):
    for j in range(5):
        array[i][j] = vetor[proximo]
        proximo += 1
        # o vetor b[i] deve conter a soma dos elementos de cada linha
        varbe[i] += array[i][j]
        
        # o vetor c[i] deve conter a soma dos elementos de cada coluna
        varce[j] += array[i][j]
        
for i in range(4):
    totvarbe += varbe[i]

for i in range(5):
    totvarce += varce[i]

total2 = totvarbe + totvarce

print ("|----------------------------------+-------|")
for i in range(4):
    for j in range(5):
        print ("| %4d " %(array[i][j]), end ="")
    #print "",
    print ("| = %4d|" %(varbe[i]) )
print ("|----------------------------------+-------|")

for j in range(5):
    print ("| %4d " %(varce[j]), end="")
print ("|       |")
print ("|------------------------------------------|")
print ("| %5d = soma dos vetores B e C           |\n| B = soma dos elementos de cada linha     |\n| C = soma do elementos de cada coluna     |" %(total2) )
print ("|------------------------------------------|")
