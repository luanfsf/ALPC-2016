#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random


loja = [[random.randrange(1, 100, 1) for i in range(4)] for j in range(12)]
mes = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

totmes = [0] * 12
totsem = [0] * 12
total = 0

for i in range(12):
    for j in range(4):
        totmes[i] += loja[i][j]
        totsem[j] += loja[i][j]
        total += loja[i][j]

print "|--s1----s2----s3----s4-|---vendas por mes-|"
for linha in range(12):
    for coluna in range(4):
        print "| %3d" %loja[linha][coluna],
    print "| %010s | %3d |" %(mes[linha], totmes[linha] ),    
    print ""
print "|-%3d---%3d---%3d---%3d-|-----Total->-%4d-|" %(totsem[0], totsem[1], totsem[2], totsem[3], total)
