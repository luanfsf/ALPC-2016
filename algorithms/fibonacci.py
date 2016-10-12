#!/usr/bin/env python
numero = 0

while ( numero < 1 or numero > 40):
  print ("digite um numero de 1 a 40")
  numero = int(input())

def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)
  
for i in range(1, numero +1):
  print i, ":", fibonacci(i) 
