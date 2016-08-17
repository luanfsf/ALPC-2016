#!/usr/bin/env python
__author__ = 'Luan'
'''Faca um programa que receba a temperatura media de cada
mes do ano e armazene-as em um vetor. Calcule e mostre a
maior e a menor temperatura do ano e em que mes elas
ocorreram  mostrar o mes por extenso: 1 Janeiro, 2 
Fevereiro. Desconsidere empates'''

mes = [0,0,0,0,0,0,0,0,0,0,0,0]
mesextenso = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]


maiortemp = 0
menortemp = 100.00

for i in range(0,12):
  print "Digite a temperatura media do mes", mesextenso[i]
  mes[i] = float(input())
  
  #menortemp = mes[i]
  
  if mes[i] > maiortemp:
    maiortemp = mes[i]
    maiortempextens = mesextenso[i]
    
  if mes[i] < menortemp:
    menortemp = mes[i]
    menortempextens = mesextenso[i]

print "O mes com a temperatura mais alta foi", maiortempextens, "com:", maiortemp
print "O mes com a temperatura mais baixa foi", menortempextens, "com:", menortemp