#!/usr/bin/env python


'''Faca um programa para corrigir provas de multipla
escolha com somatoria. Cada prova tem dez questoes e
cada questao vale 1 ponto. O primeiro conjunto de dados
a ser lido e o gabarito da prova. Os outros dados serao
os numeros dos alunos e sua respectivas respostas.
Existem 15 alunos matriculados. Calcule e mostre:
a. Para cada aluno seu numero e sua nota;
b. A percentagem de aprovacao, sabendo-se que a nota
minima e 6,0'''

gabarito = [ ]

for i in range (10):
  print "digite a resposta do gabarito - A B C D -"
  gabarito[i] = input()

for j in range (15):
  aluno = 1
  print "aluno", aluno[j]
  aluno = aluno + 1
  
  for h in range (10):
    print "digite a resposta - A B C D -"
    resposta[h] = input()
    nota = 0
    if resposta[h] == gabarito[i]:
      nota = nota + 1
  print "nota do aluno ", aluno[j], nota
  if nota >= 6:
    print "aprovado"
  if nota < 6:
    print "reprovado"