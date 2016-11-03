#!/usr/bin/env python
#python 2.7
numero = 0

while ( numero < 1 or numero > 1000):
  print ("digite um numero de 1 a 1000")
  numero = int(input())

valores = {}  
def fibonacci(n):
  if n in valores:
    return valores[n]
  
  if n == 1:
    valor  = 1
  elif n == 2:
    valor = 1
  elif n > 2:
    valor = fibonacci(n-1) + fibonacci(n-2)
  
  valores[n]= valor
  return valor
  
for i in range(1, numero + 1 ):
  print ( i, ": %i " %(fibonacci(i)) )
  #FORMATED ON THE RIGHT print i, ": %50i " %(fibonacci(i))
  #HEXADECIMAL print i, ": %x " % (fibonacci(i))
