#!/usr/bin/env python

#Loop para 30 clientes

clientes = [0] * 30
ceps = [0] * 30
valvendas [0] * 30


contvendas = 0

combo10 = 20
combo30 = 60
combo50 = 90


while contvendas < 30: # assim e possivel realizar 30 pedidos passando pelas outras opcoes
  print "1-Realizar pedido"
  print "2-Consultar maior e menor pedido"
  print "3-Consutar quantidade de pedidos de cada combo >=2"
  print "4-Consultar o total das vendas"
  
  opcao = int(input())
  
  if opcao == 1:
    """realizar pedido
    CEP
    combo (combo10, combo30, combo50)
    quntidade do combo"""
    contvendas =+ 1 # somente se o cliente realizar um pedido o contador sera incrementado
    
  if opcao == 2:
    # CEP do maior e do menor pedido
    
  if opcao == 3:
    """exibir quantos pedidos foram feitos
    de cada um dos 3 combos, se a quantidade
    for > que 1."""
        
  if opcao == 4:
    #total de vendas