#!/usr/bin/env python

array3x5 = [[0] * 5 for i in range(3)]

for linha in range(3):
  for coluna in range(5):
    while (array3x5[linha][coluna] > 100) or (array3x5[linha][coluna] < 1):
      print "Numero < 100, para", linha + 1, "x", coluna + 1, ":",
      array3x5[linha][coluna] = int(input())
      #array3x5[linha][coluna] = 15
    
for linha in range(3):
  print "  ------------------------------"
  for coluna in range(5):
    print "|", "%2d" % array3x5[linha][coluna],
  print "|",
  print ""