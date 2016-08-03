#!/usr/bin/env python
__author__ = 'LUAN'

maiornumacid = 0
codcidadmaior = 0

menornumacid = 99999
codcidadmenor = 0

somCIDacid = 0
somaACID2000 = 0

somacarros = 0

for contacidade in range (0,5):
  print ("Cidade:", contacidade + 1)
  
  print("Digite o codigo da cidade")
  codigo = raw_input()
  print("Digite o numero de veiculos")
  numveics = int(input()) 
  print ("digite o numero de acidentes")
  numacid = int(input())
  
  if numacid > maiornumacid:
    maiornumacid = numacid
    codcidadmaior = codigo
  
  if contacidade == 0:
    menornumacid = numacid
  
  if numveics > 2000:
    somaACID2000 = somaACID2000 + numacid
    somCIDacid = somCIDacid + 1
    
  else:
      if numacid < menornumacid:
        menornumacid = numacid
        codcidadmenor = codigo
        
somacarros = somacarros + numveics
    
print("Acidade", codcidadmaior, 
     "tem a maior quantidade de  acidentes com:", maiornumacid)

print("A cidade", codcidadmenor, 
     "tem o menor numero de acidentes como:", menornumacid)

media = somacarros / 5

print("A media de automoveis e:", media)

mediaACID = somaACID2000 / somCIDacid

print ("A media de acidentes nas cidades com mais de 2000 veiculos e:", mediaACID)