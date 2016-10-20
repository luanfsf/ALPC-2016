#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random
lojas = [[0.00]*5 for i in range(20)]

maiscaro = 0.00
prodcaro = 0
daloja = 0

for produto in range(20):
    for loja in range(5):
        lojas[produto][loja] = random.uniform(5, 47)
        if lojas[produto][loja] > maiscaro:
            maiscaro = lojas[produto][loja]
            prodcaro = produto +1
            daloja = loja + 1

print "|-------------------------------------------------|"
for loja in range(20):
    print "|prod. %2d" %(loja +1),
    for produto in range(5):
        print "| %5.2f" %(lojas[loja][produto]),
    print "|",
    print ""
print "|-------------------------------------------------|"
print "|---------| loja1 | loja2 | loja3 | loja 4| loja5 |"
print "|-------------------------------------------------|"
print "|O produto mais caro é o %2d da loja %2d            |" %(prodcaro, daloja)
print "|-------------------------------------------------|"
