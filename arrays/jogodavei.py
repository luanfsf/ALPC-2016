#!/usr/bin/env python

print "Jogo da velha"

velha = [[" "] * 3 for i in range (3) ]

while True:
  for i in range (3):
    print "\n-------------"
    for j in range (3):
      print "|", velha[i][j],
    #print "\n-----------"
    print "|",
  print "\n-------------"
  #print "\n"
  lin = int(input("Digite a linha")) - 1
  col = int(input("Digite a coluna")) - 1
  
  if lin jogador 