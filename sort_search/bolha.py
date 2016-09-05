#!/usr/bin/env python
__author__ = 'Luan'

numeros =  [8,5,7,4,9,6,10,1,3,2]

print "desordenados"

for i in range (10):
  print numeros[i],

for i in range (0,10):
  for j in range (i+1,10):
    if numeros[i] > numeros[j]:
      aux = numeros[i]
      numeros[i] = numeros[j]
      numeros[j] = aux
print ""      
print "Ordenados"

for i in range (10):
  print numeros[i],