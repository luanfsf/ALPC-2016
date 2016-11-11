#!/usr/bin/env python
# encoding: utf-8
# python 2.7
import random

V = [random.randrange(1, 999, 1) for i in range(18)]
A = [[0] * 6 for i in range(3)]

print ("|-----------------------------------------------------------------------------------------|")
for i in range(18):
    print ("| %3d" %(V[i]), end="")
print ("|")
print ("|-----------------------------------------------------------------------------------------|")

n = 0
for i in range(3):
    for j in range(6):
        A[i][j] = V[n]
        n += 1

for i in range(3):
    print ("\033[92m|-----------------------------|")
    for j in range(6):
        print ("| %3d" %(A[i][j]), end="")
    print ("|")
print ("|-----------------------------|")
