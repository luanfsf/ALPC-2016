#!/usr/bin/env python
# python 3.5
vendas = [[0] * 4 for i in range(5)]

for linha in range(5):
  print ("vendedor", linha )
  for coluna in range(4):
    print ("semana")
    print ("digite o valor")
    vendas[linha][coluna] = float(input())

#print "linha x coluna"
TOTAL = 0
totalvend = 0
for linha in range(5):
  for coluna in range(4):
    totalvend = totalvend + vendas[linha][coluna]
    TOTAL = TOTAL + vendas[linha][coluna]
  print ("total de vendas e", totalvend, "do vendedor ", linha)
  totalvend = 0

vendsem = 0
for coluna in range(4):
  for linha in range(5):
    vendsem = vendsem + vendas[linha][coluna]
  print ("TOTAL vendas por semana", vendsem, "na semana", coluna )
  vendsem = 0
  
print ("Total = ", TOTAL)