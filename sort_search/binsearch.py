#!/usr/bin/env python

numeros = [0] * 20

for i in range (20):
  print "Digite qualquer numero"
  numeros[i] = int(input())
  
for i in range (0,19):
  
  for j in range (i+1,20):
    
    if numeros[i] > numeros[j]:
      aux = numeros[i]
      numeros[i] = numeros[j]
      numeros[j] = aux
    pass

print "digite o numero p"
np = int(input())

inicio = 0
fim  = 19

while (inicio <= fim):
  meio = ( (fim + inicio) / 2 )
  print "ini:", inicio, "fim:", fim, "meio", meio
  if np == numeros[meio]:
    print "Encontrado [",meio,"]"
    break
  else:
    if np > numeros[meio]:
      inicio = meio + 1
    else:
      if np < numeros[meio]:
        fim = meio - 1
        