#include <cs50.h>
#include <stdio.h>

int numero = 0;

int fib(int x);

int main(){
    
    while (numero < 1 || numero > 46){
        printf ("digite um numero de 1 a 46: ");
        /* 46 e o maior numero que C suporta nessa funcao 1836311903
        o próximo seria  (2971215073), mas ele excede o limite de
        2^(32-1) que e de(2147483648).
        */
        numero = GetInt();
    }
    
    for (int i = 1; i < numero; i++){
        printf ("%i \n", fib(i) );
    }
    
    return 0;
}

int fib(int x){
    if (x == 1){
        return 1;
    }
    if (x == 2){
        return 2;
    }
    return fib(x - 1) + fib(x - 2);
}