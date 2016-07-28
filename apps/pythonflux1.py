#!/usr/bin/env python
print("digite um numero")
num1 = int(input())
print("digite outro numero")
num2 = int(input())
if num1 == num2:
    print("sao iguais")
    print("e sua media e")
else:
    print("nao sao iguais")
    if num1 > num2:
      print ("Num1 maior:",num1)
    else:
      print ("Num2 maior",num2)