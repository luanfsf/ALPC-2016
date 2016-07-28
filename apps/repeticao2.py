#!/usr/bin/env python
novos = 0
somaidades = 0
somaalturas = 0
for time in range (0,5):
  print ("Time:" time + 1)
  for jogador in range (0,11):
  print ("A idade")
  idade = int(input())
  print ("O peso")
  peso = float(input())
  print ("A altura")
  altura = float(input())
  
  if idade < 18:
    novos = novos + 18
  somaidades = somaidades + idade  
  
mediaidades = somaidades / 11

mediaaltura = somaalturas / 55
print ("Os jogadores menores de 18 e;", novos)




'''
REPREP2)Em um campeonato de futebol existem cinco times e cada time possui onze jogadores. Faça um programa que receba a idade, o peso e a altura de cada um dos jogadores, calcule e mostre (valide todos os dados de entrada):
- a quantidade de jogadores com idade inferior a 18 anos;
- a média das idades dos jogadores de cada time;
- a média das alturas de todos os jogadores do campeonato;
- a percentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato.
'''