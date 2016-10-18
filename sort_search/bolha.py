#!/usr/bin/env python
__author__ = 'Luan'
import random

#numeros =  [8,5,7,4,9,6,10,1,3,2,50,40,60,15,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
#           44,41,42,43,45,46,47,48,49,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
#numeros = [random.randrange(1,101,1) for _ in range (100)]
#sample(range(10000000), 60)

print "digite o numero de numeros aleatorios"
qnumeros = int(input())

#isso aqui ta funcionando mas ainda esta gerando numeros repetidos
# os numeros aleatorios sao entre 10 vezes o numero de numeros aleatorios

numeros = [random.randrange(1,10*qnumeros,1) for _ in range (qnumeros)]
print len(numeros)

print "desordenados"

for i in range (len(numeros)):
  print numeros[i],

for i in range (len(numeros)):
  for j in range (i+1,len(numeros)):
    if numeros[i] > numeros[j]:
      aux = numeros[i]
      numeros[i] = numeros[j]
      numeros[j] = aux
print ""      
print "Ordenados"

# aqui a lista continua tendo os itens repetidos mas so exibe os unicos
#print set (numeros)

# se numeros repetido forem gerados eles serao exibidos lado a lado
print numeros

#for i in range (len(numeros)):
#  print numeros[i],