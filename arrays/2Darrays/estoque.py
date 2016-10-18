#!/usr/bin/env python
# encoding: utf-8
# python 2.7

array5x3 = [[-1] * 3 for i in range(5)]
maiorstoqprod2 = 0
armz2 = 0
menorestoque = 0
vendmenor = 0
contprod = [0] * 3
contarmaz = [0] * 4
totcontarmaz = [0.00] * 4

for i in range(3):
    while array5x3[4][i] < 0.01 or array5x3[4][i] > 9.99:
      print "Digite o valor do produto %2d:" %(i+1),
      array5x3[4][i] = float(input())
    
    #array5x3[4][i] = 3.57 #constante para nao ter que digitar cada valor

for armazem in range(4):
  for produto in range(3):
    while ( array5x3[armazem][produto] <= 0 or array5x3[armazem][produto] > 999):
      print "Digite a quantidade do produto:", produto + 1, "do armazém", armazem + 1, ":",
      array5x3[armazem][produto] = int(input())
      #array5x3[armazem][produto] = 26 #constante para nao ter que digitar cada valor
    contprod[produto] += array5x3[armazem][produto]
    contarmaz[armazem] += array5x3[armazem][produto]
    totcontarmaz[armazem] += array5x3[armazem][produto] * array5x3[4][produto]
    
    if produto == 1:
      if array5x3[armazem][produto] > maiorstoqprod2:
        maiorstoqprod2 = array5x3[armazem][produto]
        armz2 = armazem

print "\n|------------------------------|"
for armazem in range(5):
  if armazem == 0:
    print "|-prod1--prod2--prod3|         |"
  elif armazem == 4:
    print "|_valor dos produtos_|         |"
  else:
    print "|--------------------|         |"
  for produto in range(3):
    if armazem == 4:
      print "|", "%0.2f" %array5x3[armazem][produto],
    else:
      print "|", "%4d" %array5x3[armazem][produto],
  if armazem != 4:
    print "|>Armz:", armazem+1, "|",
  else:
    print "|         |",
  print ""
print "|------------------------------|"

print "\n---RESULTADOS------------------------------------"
print "\nA) Itens por armazém" 
for i in range(4):
  print "   Armazém", (i+1), ":", contarmaz[i]
  if i == 0:
    menorestoque = contarmaz[i]
  if contarmaz[i] < menorestoque:
    menorestoque = contarmaz[i]
    vendmenor = i
  
print "\nB) O maior estoque do produto2 é do armazém:", armz2 +1
print "\nC) O armazém com menor estoque é o:", vendmenor +1

print "\nD) O custo total de cada produto é:"
for i in range(3):
  print "   Produto ",(i+1), ":",  contprod[i] * array5x3[4][i]

print "\nE) O custo de cada armazém é: "
for i in range(4):
  print "   Armazém",(i+1), ":", totcontarmaz[i]
print "-------------------------------------------------"