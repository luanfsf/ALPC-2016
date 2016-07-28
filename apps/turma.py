#!/usr/bin/env python

contador = 0
maisvelho = 0
maisnovo = 100
# maisnovo = idade
while contador < 10:
  print ("digite a idade da crianca")
  idade = int(input())
  if idade < maisnovo:
    maisnovo = idade
  if idade > maisvelho:
    maisvelho = idade
  contador = contador + 1
print ("A crianca mais velha e", maisvelho)
print ("A crianca mais nova e", maisnovo)