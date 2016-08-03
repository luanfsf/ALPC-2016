#!/usr/bin/env python

maisalto = 0
menosalto = 0
somaaltf = 0
contf = 0

print "digite o numero de pessoas"
npessoas = int(input())

for pessoa in range (0,npessoas):
    print("pessoa:", pessoa +1)
    print ("digite a altura")
    altura = float(input())
    print ("Digite o sexo f=feminino e m=masculino")
    sexo = raw_input()
    
    if sexo == 'f' or sexo == 'F':
      somaaltf = somaaltf + altura
      contf = contf + 1
    
    if altura > maisalto:
        maisalto = altura
        sexomaisalto = sexo 
    
    if pessoa == 0:
        menosalto = altura
    
    else:
        if altura < menosalto:
          menosalto = altura
        
  # if altura < menosalto:
      # menosalto = altura
    
print ("o mais alto e: %.2f" % maisalto)
print ("o menos alto e: %.2f" % menosalto)

mediasltf = somaaltf / contf

print "a media da altura feminina e: ", mediasltf