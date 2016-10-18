#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import  random

somaimpares = 0
somapares = 0
total = 0.00

numeros3x4 = [[random.randrange(1, 100, 1) for i in range(4)] for j in range(3)]
#numeros = [random.randrange(1, 100, 1) for _ in range (10)] #inteiros

#numeros = [[random.random() for i in range(4)] for j in range(3)] # numeros float
#numeros = [[random.random() for x in xrange(N)] for y in xrange(N)]

for linha in range(3):
  print "|-----------------------|"
  for coluna in range(4):
    print "|%3d " %numeros3x4[linha][coluna],
    if numeros3x4[linha][coluna] % 2 == 0 :
      somapares += 1 #numeros3x4[linha][coluna]
    else:
      somaimpares += numeros3x4[linha][coluna]
    total += numeros3x4[linha][coluna] 
  print "|",
  print ""
total = total/(3*4) 
print "|-----------------------|"
print "|Existem%3d pare(s)     |" %somapares
print "|Impares somados = %3d  |" %somaimpares
print "|A media totals é %0.2f |" %total
print "|-----------------------|"

# Faça um programa que carregue uma matriz 3 x 4, calcule e mostre:
# A quantidade de elementos pares
# A soma dos elementos ímpares
# A média de todos os elementos
