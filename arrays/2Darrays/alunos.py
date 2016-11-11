#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

#disciplinas = random.sample(range(250), 5)
idadealunos = [random.randrange(15,35, 1) for i in range(8)]

disciplinas = ["ALPC","FENS","CALC","ARQT","MTDC"] 
# for i in range(5):
#     print "Digite o código da disciplina:"
#     disciplinas[i] = int(input())
    
prova = [[0] * 5 for i in range(8)]

for aluno in range(8):
    for materia in range(5):
        prova[aluno][materia] = random.randrange(0,6, 1)
        # O que falta ser feito é que o código de cada matéria não deve ser repetido
        # if idadealunos[aluno] >= 18 and idadealunos[aluno] <= 25: for materia in range(5):
        #     if prova[aluno][materia] > 2:
        #         entre18e25 += 1     # para armazenar a quantidade dealunos com idade entre 18 e 25 anos e 
        #         break               # que fizeram mais de duas provas em todas as disciplinas
print ("+------------------------------------------+")
for aluno in range(8):
    if aluno == 0:
        print ("\033[94m|Aluno |Idade", end="")
        for i in range(5):
            print ("|%4s "  %(disciplinas[i]), end ="" )
        print ("|", end="")
        print ("")
    print ("\033[92m| %2d  | %3d  " %(aluno +1 , idadealunos[aluno]), end="")
    for materia in range(5):
        print ("\033[0m| %2d  " %(prova[aluno][materia]), end="")
    print ("|", end ="")
    print ("")
print ("+------------------------------------------+")
print ("\033[94m| Alunos com idades entre 18 e 25 anos que |")
print ("| fizeram mais de duas provas por materia. |")
entre18e25 = 0
for materia in range(5):
    print ("\033[92m| %4s  " %(disciplinas[materia]), end="")
    for aluno in range(8):
        if idadealunos[aluno] >= 18 and idadealunos[aluno] <= 25:
            if prova[aluno][materia] > 2:
                entre18e25 += 1
    print ("| %2d |\033[0m *************************** |" %(entre18e25) )
    entre18e25 = 0    
print ("+------------------------------------------+")
print ("\033[94m| Alunos com menos de 3 provas por materia |")
for aluno in range(8):
    print ("\033[92m| %2d " %(aluno+1), end="")
    for materia in range(5):
        if prova[aluno][materia] < 3:
            print ("|\033[91m %4s " %(disciplinas[materia]), end="")
    print ("|", end="")    
    print ("")
            
print ("\033[0m+------------------------------------------+")
qntnfz = 0
mdqntnfz = 0.00
for aluno in range(8):
    for materia in range(5):
        if prova[aluno][materia] == 0:
            mdqntnfz += idadealunos[aluno]
            qntnfz += 1
            break
print ("\033[94m| A média da idade dos alunos que deixaram |")
print ("| de fazer alguma prova é %2.2f            | " %(mdqntnfz / qntnfz) )
print ("\033[0m+------------------------------------------+" )