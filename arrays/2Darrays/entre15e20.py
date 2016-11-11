#!/usr/bin/env python
# python 2.7
import random
array3x5 = [[0] * 5 for i in range(3)]
x = 0

for linha in range(3):
  for coluna in range(5):
    while (array3x5[linha][coluna] > 50) or (array3x5[linha][coluna] < 1):
      #print "Numero positivo <= 50, para", linha + 1, "x", coluna + 1, ":",
      #array3x5[linha][coluna] = int(input())
      array3x5[linha][coluna] = random.randrange(1, 50, 1)
      if (array3x5[linha][coluna] <= 20) and (array3x5[linha][coluna] >= 15):
        x = x + 1
    
for linha in range(3):
  print ("+------------------------+")
  for coluna in range(5):
    print ("|", "%2d " % array3x5[linha][coluna], end="")
  print ("|", end="")
  print ("")
print ("+------------------------/ Existem %2d numero(s) entre 15 e 20 inclusive, nessa matriz" %x )