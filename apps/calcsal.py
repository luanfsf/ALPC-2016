#!/usr/bin/env python
__author__ = 'Walter'
'''Construir um programa que efetue o calculo do
salario liquido de um professor. Para fazer este
programa, voce devera possuir alguns dados, tais
como: valor da hora aula, numero de horas trabalhadas
no mes e percentual de desconto do INSS. Em primeiro
lugar, deve-se estabelecer qual sera o seu salario
bruto para efetuar o desconto e ter o valor do salario
liquido.'''
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
