#!/usr/bin/env python
__author__ = 'LUAN'

cidademaioracidente = 0
cidademenoracidente = 99999
maiornumacid = 0
menornumacid = 9999

for contacidade in range (0,5):
  print
  ("cidade:" contacidade + 1 )
  codigo = int(input())
  print ("digite o numero de veiculos")
  muveic = int(input())
  print ("digite o numero de acidentes")
  numacid = int(input())
  
  if numacid > maiornumacid:
    maiornumacid = numacid
    cidademaioracidente = codigo
  
  if contacidade == 0:
    menornumacid = numacid
    cidademenoracidente
    
  else:
    if numacid < cidademenoracidente:
    menornumacid = numacid
    
    
print ("a cidade", cidademaioracidente, 
      "tem a maior quantidade de acidentes com" maiornumacid)
print ("a cidade", cidademenoracidente,
      "tem a menor quantidade de acidentes com" )
print ("")