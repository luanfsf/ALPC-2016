#!/usr/bin/env python

velha = [[" "] * 3 for i in range (3) ]
print "Jogo da velha!"
print "X comeca",

linha = 1
coluna = 1
jogador = 1
fim = 1

while (fim != 0):
  print "digite o local de acordo com a tabela"
  print "    1  2  3"
  print " 1  _  _  _"
  print " 2  _  _  _"
  print " 3  _  _  _"
  
  ok = 1
  while (ok != 0):
    # caso o jogador digite uma posicao ocupada ele continuara nesse loop
    print "Jogador:",jogador
    print "Linha:"
    linha = int(input())
    print "Coluna:"
    coluna = int(input())
    if jogador == 2 and velha[linha-1][coluna-1] != "X" and velha[linha-1][coluna-1] != "O":
      velha[linha-1][coluna-1] = "O"
      jogador -= 1 # essa "logica" e pra trocar de usuario
      ok = 0
    if jogador == 1 and velha[linha-1][coluna-1] != "X" and velha[linha-1][coluna-1] != "O":
      velha[linha-1][coluna-1] = "X"
      jogador += 1 # essa "logica" e pra trocar de usuario
      ok = 0
      
  print "\n--------------------------------------"
  for i in range (3):
    print "\n-------------"
    for j in range (3):
      print "|", velha[i][j],

    print "|",
  print "\n-------------"

  if (velha[0][0] == "X" and velha[0][1] == "X" and velha[0][2] == "X") or
  (velha[1][0] == "X" and velha[1][1] == "X" and velha[1][2] == "X") or
  (velha[2][0] == "X" and velha[2][1] == "X" and velha[2][2] == "X") or
  (velha[0][0] == "X" and velha[1][1] == "X" and velha[2][2] == "X") or
  (velha[0][2] == "X" and velha[1][1] == "X" and velha[2][0] == "X"):
    print "X venceu!"
    fim = 0
  if (velha[0][0] == "O" and velha[0][1] == "O" and velha[0][2] == "O") or
  (velha[1][0] == "O" and velha[1][1] == "O" and velha[1][2] == "O") or
  (velha[2][0] == "O" and velha[2][1] == "O" and velha[2][2] == "O") or
  (velha[0][0] == "O" and velha[1][1] == "O" and velha[2][2] == "O") or
  (velha[0][2] == "O" and velha[1][1] == "O" and velha[2][0] == "O"):
    print "O venceu!"
    fim = 0
