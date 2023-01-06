#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <direct.h>

void delay(int num)
{
    int milli_seg = 1000 * num;

    clock_t start = clock();

    while (clock() < start + milli_seg);
}

int main()
{
    int area[20];
    int l, c, lin=0, col=0, a, cont=0, j;


printf("\n\n ----------------- Entrada de dados ---------------- \n\n");


int matriz[4][5]= {{1, 0, 1, 0, 0},
                   {1, 0, 1, 1, 1},
                   {1, 1, 1, 1, 1},
                   {1, 0, 0, 1, 0}};

    for(l=0; l < 4; ++l){
        for(c=0; c < 5; ++c)
        {
            printf("%i ", matriz[l][c]);
        }
        printf("\n");
        }

    for(l=0; l < 4; ++l){
        for(c=0; c < 5; ++c)
        {
            if (matriz[l][c]){}
        }}


printf("\n\n -------------Saída de dados------------- \n\n");
delay(1);

printf("\n O valor da area de maior quadrado e: %i", a);
delay(2);

    return 0;
}
