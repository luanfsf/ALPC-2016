#!/usr/bin/env python

print("Digite o valor da venda media mensal")
vendprod = float(input())
print("Digite o preco atual")
precprod =float(input())
if vendprod < 500 or precprod < 30:
  porcprec = precprod * 12
  porcprecdiv = porcprec /100
  novopreco = precprod + porcprecdiv
else:
  if (vendprod >= 500 and precprod < 1600):
      or (precprod >= 30 and precprod < 80):
  else:
      if vendprod >= 1600 or precprod >= 80:
      #desconto
      novopreco= precprod - (precprod * 25 )
      novoprecodiv = novopreco / 100
print ("O novo preco e:   %.4f" % novoprecodiv)