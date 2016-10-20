#!/usr/bin/env python
# encoding: utf-8
# python 2.7

import random

notalunos = [[0] * 3 for i in range(10)]

for aluno in range(10):
    for nota in range(3):
        #print "Digite a nota do aluno:", aluno+1
        #notalunos[aluno][nota] = 5.5
        notalunos[aluno][nota] = random.uniform(5, 10) 
        #notalunos[aluno][nota] = float(input())
print "\n|--------------------------------------|"
print "|-RESULTADOS--------PRV1---PRV2---PRV3-|"
for aluno in range(10):
    #print "|--------------------------------------|"
    print "| Aluno %2d" %(aluno + 1),
    print "notas:",
    for nota in range(3):
        print "| %0.2f" %notalunos[aluno][nota],
    print "|"
print "|--------------------------------------|"

prova = [0]*3


print "|-MENORES NOTAS-----PRV1---PRV2---PRV3-|"
for aluno in range(10):
    print "| Aluno %2d:" %(aluno + 1),
    print "menor",
    for nota in range(3):
        for notabaixa in range(3):
            if notabaixa == 0:
                menornota = notalunos[aluno][notabaixa]
            if notalunos[aluno][notabaixa] < menornota:
                menornota = notalunos[aluno][notabaixa]
                
        if notalunos[aluno][nota] == menornota:
            print "| %0.2f" %notalunos[aluno][nota],
            prova[nota] += 1
        else:
            print "|     ",
    print "|" #fim do bloco
    if aluno == 9:
        print "|--------------------------------------|"
        print "|TOT notas baixas-|  %2d  |  %2d  |  %2d  |" %(prova[0], prova[1], prova[2])
print "|--------------------------------------|"
