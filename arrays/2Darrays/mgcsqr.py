#!/usr/bin/env python
# encoding: utf-8
# python 3.5
dimensao = 3
mgcsqr = [[1,2,3],[4,5,6],[7,8,9]]
ganhou = False

print ("\033[92m|------------------------------------------------------|")
print ("\033[92m| QUADRADO MÁGICO!      não escalável :-(              |")
print ("\033[92m|------------------------------------------------------|")

while ganhou == False:
    L1,L2,L3, C1,C2,C3, D1,D2 = (0,0,0,0,0,0,0,0)
    
    D1 = mgcsqr[2][0] + mgcsqr[1][1] + mgcsqr[0][2]
    D2 = mgcsqr[0][0] + mgcsqr[1][1] + mgcsqr[2][2]
    
    L1 = mgcsqr[0][0] + mgcsqr[0][1] + mgcsqr[0][2]
    L2 = mgcsqr[1][0] + mgcsqr[1][1] + mgcsqr[1][2]
    L3 = mgcsqr[2][0] + mgcsqr[2][1] + mgcsqr[2][2]
    
    C1 = mgcsqr[0][0] + mgcsqr[1][0] + mgcsqr[2][0]
    C2 = mgcsqr[0][1] + mgcsqr[1][1] + mgcsqr[2][1]
    C3 = mgcsqr[0][2] + mgcsqr[1][2] + mgcsqr[2][2]
        
    print ("\033[92m|------------------------------------------------------|")
    if D1 != 15:
        print ("\033[92m|--------------|\033[91m=%2d \033[92m>>> diagonal                       |" %(D1) )
    else:
        print ("\033[92m|--------------|=%2d >>> diagonal                       |" %(D1) )
    
    for lin in range(dimensao):
        for col in range(dimensao):
            print ("|%3d" %(mgcsqr[lin][col]), end="")
            
        if lin == 0 :
            if L1 != 15:
                print ("|\033[91m = %2d \033[92m|                                   |" %(L1) )
            else:
                print ("| = %2d |                                   |" %(L1) )
        if lin == 1 :
            if L2 != 15:
                print ("|\033[91m = %2d \033[92m|                                   |" %(L2) )
            else:
                print ("| = %2d |                                   |" %(L2) )
        if lin == 2 :
            if L3 != 15:
                print ("|\033[91m = %2d \033[92m|                                   |" %(L3) )
            else:
                print ("| = %1d |                                   |" %(L3) )
    
    if D2 != 15:
        print ("\033[92m|-  -|-  -|-  -|\033[91m=%2d \033[92m>>> diagonal                       |" %(D2) )
    else:
        print ("\033[92m|-  -|-  -|-  -|=%2d >>> diagonal                       |" %(D2) )
    
        
    #print "\033[92m|-%2d-|-%2d-|-%2d-|" %(C1, C2, C3)
    
    if C1 != 15:
        print ("| \033[91m%2d\033[92m" %(C1), end="")
    else:
        print ("| %2d" %(C1), end="")
    
    if C2 != 15:
        print ("| \033[91m%2d\033[92m" %(C2), end="")
    else:
        print ("| %2d" %(C2), end="")
    
    if C3 != 15:
        print ("| \033[91m%2d \033[92m|                                         |" %(C3) )
    else:
        print ("| %2d|                                          |" %(C3) )
    
    if L1 == 15 and L2 == 15 and L3 == 15 and C1 == 15 and C2 == 15 and C3 == 15 and D1 == 15 and D2 == 15:
        ganhou = True 
        print ("| Você ganhou!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! |")
        break
    
    #if todas as posicoes sao iguais a 15 entao True
    print ("\033[92m|------------------------------------------------------|")
    print ("| Digite dois numeros para serem trocados de posição:  |", end="")
    primeiro = 0
    segundo = 0
    while primeiro < 1 or primeiro > 9:
        primeiro = int(input())
        while segundo < 1 or segundo > 9:
            segundo = int(input())

    for i in range(dimensao):
        for j in range(dimensao):
            if mgcsqr[i][j] == primeiro:
                posprii = i
                posprij = j
            if mgcsqr[i][j] == segundo:
                possegi = i
                possegj = j
    mgcsqr[posprii][posprij] = segundo
    mgcsqr[possegi][possegj] = primeiro
    
print ("\033[92m|------------------------------------------------------|")
