#!/usr/bin/env python
print("Digite um numero de 2 a 10 para ver a tabuada")
# na verdade pode digitar quallquuer numero
contador = int(input())
multiplicador = contador
print " "
print "Tabuada de", multiplicador
print " "
numero = 1
while  numero <= 10:
#while contador <= ___ or numero < 10: ------ assim tambem funciona
  print  multiplicador, " x" , numero, "=", contador
  contador = contador + multiplicador
  numero = numero + 1  