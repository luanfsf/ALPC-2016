#!/usr/bin/env python

print("digite o valor do salario minimo")
salmin = int(input())
print("digite o gasto de quilowatts por mes")
qwtgst = int(input())
#quilowatt e um quinto do  salario minimo
quilwat = salmin/5
print "Valor do quilowatt e",quilwat 
#o valor apagar (qwtpgr) e o quilowatt gasto (qwtgst) x o valor do quilwat (quilwat)
qwtpgr = qwtgst * quilwat
print "Valor a pagar e",qwtpgr
#o desconto e quantidade a pagar (qwtpgr) x 15 / 100
#calculo 1
descqwt = qwtpgr * 15
#calculo 2
descqwtf = descqwt/100
# o valor a  pagar com desconto(pgrdesc) e o valor a pagar (qwtpgr) menos o valor do desconto (desqwtf) 
pgrdesc = qwtpgr - descqwtf
print "Valor a pagar com desconto e",pgrdesc

#da erro quando tem letras com acentos

raw_input("prompt:")

#raw_input("prompt: ") comando para evitar que o app feche sem mostar o calculo