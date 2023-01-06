#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>


void tempo(int num)
{
    int milli_seg = 1000 * num;

    clock_t start = clock();

    while (clock() < start + milli_seg)
        ;
}


int conta_txt(char *txt, char caracter){
    int cont = 0, i;

    for (i=0; txt[i] != '\0'; i++) {
        if (txt[i] == caracter){
            cont++;
        }
    }

return cont;
}

int achar_txt(char *txt, char caracter){

    int cont = 0, i=0 , res= 0, ant = 0;


    for (i=0; txt[i] != '\0'; i++) {
        if (txt[i] == caracter){
            res = i;
        }
    }
    return res;
}


char main()
{

    int op = 1, num1, num2, num3, num4, res1, res2;
    char  Str1 = '(', Str2 = ')';
    double Str[1000];


    printf("\nPrimeira entrada de dados: \n");
    tempo(2);
    printf("Digite a frase a ser analisada: \n");
    tempo(2);
    gets(Str);
    tempo(2);
    num1 = conta_txt(Str, Str1);
    num2 = conta_txt(Str, Str2);
    if (num2 == num1){
        res1 = 1;
    } 
    else{
        res1 = 0;
    }
    num3 = achar_txt(Str, Str1);
    num4 = achar_txt(Str, Str2);
    if (num3 < num4 || num3 == num4){
        res2 = 1;
    }
    else {
        res2 = 0;
    }
    if (res1 == 1 && res2 == 1){
        printf("\n1");
        return Str;
    }
    else {
        if(res1 == 0 && res2 == 1){
        printf("\n0");
        return Str;
    } else
        printf("\n0");
    }
    tempo(2);
}