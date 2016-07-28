#!/usr/bin/env python
salario = 0
for ano in range (1995, 2017):
  if ano == 1995:
    salario = 1000
  if ano == 1996:
      perc  = 1.5
  print ("Ano:", ano , "salario:", salario)
  valaumento = (salario * perc) / 100
  salario = salario + valaumentof