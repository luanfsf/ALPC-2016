#!/usr/bin/env python

# nao funcionou esse programa
tot_alunos = 0
N_turma_turma = 0
N_masc = 0
N_femi = 9999
print ("digite o numero de turmas")
nturmas = int(input())
for turmas in range (nturmas):
  print "turma:", turmas +1
  print ("digite o numero da sala")
  sala = int(input())
  print ("digite o numero de alunos")
  nalunos = int(input())
  tot_alunos = tot_alunos + nalunos
  
  masc = 0
  femi = 0
  
  
  for alunos in range(nalunos):

    print  ("digite o sexo de cada aluno M ou F")
    sexo = raw_input()
    print "aluno:", alunos +1

    if sexo == "M" or sexo == "m":
      masc = masc + 1
      print masc
      if masc > N_masc:
        N_masc = masc
        N_turma_masc = sala
        
    if sexo == "F" or sexo == "f":
      femi = femi + 1
      print femi
      if femi < N_femi:
        N_femi = femi
        N_turma_femi = sala
        
    
media_alunos = tot_alunos / nturmas
print "A. O numero total de alunos na creche e :", tot_alunos
print "B. A media de alunos por turma e:", media_alunos
print 'C. A sala com maior numero de meninos e:', N_turma_masc, "com", N_masc
print 'D. A sala com menor numero de meninas e:', N_turma_femi, "com", N_femi