#!/usr/bin/env python
print("sua idade e")
idade = int(input())
if idade <=20:
    print("Jovem")
else:
    if idade >= 21 and idade < 70:
        print ("Adulto")
    else:
        print("Idoso")