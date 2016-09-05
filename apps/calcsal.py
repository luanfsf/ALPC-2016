#!/usr/bin/env python

print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trabalhadas")
numhoras = float(input())
print("Digite o percentual de desconto do INSS")
percdesc = float(input())
salbruto = valhora * numhoras
print("O valor do salario bruto e: ", salbruto)
valdesc = (salbruto * percdesc) / 100
salliq = salbruto - valdesc
print("O valor do salario liquido e: ", salliq)
