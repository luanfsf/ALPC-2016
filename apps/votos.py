#!/usr/bin/env python
totcand1 = 0
totcand2 = 0
totcand3 = 0
totcand4 = 0
for contador in range (0,10):
    print("Digite seu voto")
    voto = int(input()) 
    if voto == 1:
        print ("Voto candidato 1")
        totcand1 = totcand1 + 1
    else:
        if voto == 2:
            print ("Voto candidato 2")
            totcand2 = totcand2 + 1
        else:
            if voto == 3:
                print ("Voto candidato 3")
                totcand3 = totcand3 + 1
            else:
                if voto == 4:
                    print ("Voto candidato 4")
                    totcand4 = totcand4 + 1
                              
print "o total de votos do candidato 1 e", totcand1
print "o total de votos do candidato 2 e", totcand2
print "o total de votos do candidato 3 e", totcand3
print "o total de votos do candidato 4 e", totcand4