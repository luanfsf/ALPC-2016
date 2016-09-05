#!/usr/bin/env python

print "Digite sua altura"
altura = float(input())

print "Digite seu sexo"
sexo = raw_input()

  
if sexo == "M" or sexo == "m":
    print "Sexo Masculino..."
    pesoideal = (72.7 * altura) - 58
else:
    print "Sexo Feminino"
    pesoideal = (62.1 * altura) - 44.7
print "O seu peso ideal e: ", pesoideal
