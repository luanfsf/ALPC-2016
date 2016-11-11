#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

array5x3 = [[-1] * 3 for i in range(5)]

maiorstoqprod2 = 0 # Para o armazenamento temporario do maior estoque do produto 2
armz2 = 0 # Para o numero de quem tem mais o produto 2

menorestoque = 0 # Para o armazenamento temporario do menor estoque
vendmenor = 0 # Para o numero do armazem com menos estoque 

contprod = [0] * 3 # Para armazenar a quantidade por tipo de produtos
contarmaz = [0] * 4 # Para armazenar a quantidade de produtos por armazem
totcontarmaz = [0.00] * 4 # Para armazenar o total de cada produto vezes o respectivo preco para cada venda

for i in range(3): # repeticao para armazenar o valor dos produtos
    #array5x3[4][i] = 3.57 #constante para nao ter que digitar cada valor
    while array5x3[4][i] < 0.01 or array5x3[4][i] > 9.99:
      #print "Digite o valor do produto %2d:" %(i+1),
      #array5x3[4][i] = float(input())
      array5x3[4][i] = random.uniform(5, 10) # random valores float entre 5 e 10

for armazem in range(4): # para 4 armazens
  for produto in range(3): # para cada armazens faca 3 produtos
    #array5x3[armazem][produto] = 26 #constante para nao ter que digitar cada valor
    while ( array5x3[armazem][produto] <= 0 or array5x3[armazem][produto] > 999):
      #print "Digite a quantidade do produto:", produto + 1, "do armazém", armazem + 1, ":",
      #array5x3[armazem][produto] = int(input())
      array5x3[armazem][produto] = random.randrange(1, 100, 1) # quantidades entre 1 e 100
      
    contprod[produto] += array5x3[armazem][produto] # Para armazenar a quantidade por tipo de produtos
    contarmaz[armazem] += array5x3[armazem][produto] # Para armazenar a quantidade de produtos por armazem
    
    # Para armazenar o total de cada produto vezes o respectivo preco para cada armazem
    totcontarmaz[armazem] += array5x3[armazem][produto] * array5x3[4][produto]
    
    if produto == 1: # Para a pergunta B
      if array5x3[armazem][produto] > maiorstoqprod2:
        maiorstoqprod2 = array5x3[armazem][produto]
        armz2 = armazem

print ("\n+------------------------------+")
for armazem in range(5):
  if armazem == 0:
    print ("|-prod1--prod2--prod3|         |")
  elif armazem == 4:
    print ("|_valor dos produtos_|         |")
  else:
    print ("|--------------------|         |")
  for produto in range(3):
    if armazem == 4:
      print ("|", "%0.2f " %array5x3[armazem][produto], end="")
    else:
      print ("|", "%4d " %array5x3[armazem][produto], end="")
  if armazem != 4:
    print ("|>Armz:", armazem+1, "|", end="")
  else:
    print ("|         |", end="")
  print ("")
print ("+------------------------------+")

print ("\n---RESULTADOS------------------------------------")
print ("\nA) Itens por armazém")
for i in range(4):
  print ("   Armazém", (i+1), ":", contarmaz[i])
  if i == 0: # Condições para responder a resposta C
    menorestoque = contarmaz[i]
  if contarmaz[i] < menorestoque:
    menorestoque = contarmaz[i]
    vendmenor = i
  
print ("\nB) O maior estoque do produto2 é do armazém:", armz2 +1)
print ("\nC) O armazém com menor estoque é o:", vendmenor +1 )

print ("\nD) O custo total de cada produto é:")
for i in range(3):
  print ("   Produto ",(i+1), ":%0.3f" %( contprod[i] * array5x3[4][i] ) )

print ("\nE) O custo de cada armazém é: ")
for i in range(4):
  print ("   Armazém",(i+1), ": %0.3f" %(totcontarmaz[i]) )
print ("-------------------------------------------------")