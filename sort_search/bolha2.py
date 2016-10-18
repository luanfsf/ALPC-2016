#!/usr/bin/env python
__author__ = 'Luan'
import random

#numeros =  [8,5,7,4,9,6,10,1,3,2,50,40,60,15,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
#           44,41,42,43,45,46,47,48,49,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
#numeros = [random.randrange(1,101,1) for _ in range (100)]
#sample(range(10000000), 60)

#esse funciona mas gera numeros iguais
#numeros = [random.randrange(1,101,1) for _ in range (100)]

#numeros = [random.sample(range(1, 1000 = variacao entre os numeros), 1000= quantidade de numeros aleatorios)]
# a variacao deve ser maior que a quantidade de numeros aleatorios
numeros = [random.sample(range(1, 10000), 1000)]
# essa funcao gera numeros aleatorios na posicao numeros[0]
# ou seja os numeros aleatorios estam sendo gerados dentro 
# de uma posicao de uma lista

numerosordem = numeros[:]

print "desordenados"

for i in range (len(numeros)):
  print numeros[i],

#isso aqui nao ta funcionando
#agora ta 
for i in range (len(numerosordem[0])):
  for j in range (i+1,len(numerosordem[0])):
    if numerosordem[0][i] > numerosordem[0][j]:
      aux = numerosordem[0][i]
      numerosordem[0][i] = numerosordem[0][j]
      numerosordem[0][j] = aux
print ""      

print "Ordenando..."

print numerosordem[0]
#for i in range (len(numerosordem)):
#  print numerosordem[i],