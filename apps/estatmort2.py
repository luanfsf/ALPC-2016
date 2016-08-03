#!/usr/bin/env python

maiornumacid = 0
cidademaiornumero = 0
cidademenornumero = 0
menornumacid = 9999
somacarros = 0
somaacidentes = 0
somacidadesacidentes = 0

for contacidade in range (0,5):
    print("Cidade: ", contacidade+1)
    print("Digite o código da cidade")
    codigo = int(input())
    print("Digite o num de veiculos")
    numveic = int(input())
    print("Digite o numero de acidentes")
    numacid = int(input())
    
    if numacid > maiornumacid:
        maiornumacid = numacid
        cidademaiornumero = codigo
    
    if contacidade == 0:
        menornumacid = numacid
    
    if numveic > 2000:
    somaacidentes = somaacidentes + numacid
    somacidadesacidentes =  somacidadesacidentes + 1
    
    else:
        if numacid < menornumacid:
            menornumacid = numacid
            
    
    somacarros = somacarros + numveic
    
print("A cidade ", cidademaiornumero,
      "tem a maior quantidade de acientes com: ", maiornumacid)
print("A cidade", cidademenornumero,
      "tem a maior qtd de acidentes com: ", menornumacid)

media = somacarros / 5

print("A media de automoveis e", media)

mediaacid = somaacidentes / somacidadesacidentes

print ("a media de acidentes nas ciddades com mais  de 2000 veiculos e" mediaacid)



