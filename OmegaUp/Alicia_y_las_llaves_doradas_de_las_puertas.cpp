#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]){
    int chapa, chapas[100000] = {}, llave, ch;

    scanf("%d", &chapa);
    for(int i = 0; i < chapa; i++)
        if(scanf("%d", &ch))
            chapas[ch - 1] = i + 1;
    scanf("%d", &llave);
    
    for (int i = 0; i < llave; i++)
        if(scanf("%d", &ch) == 1)
            printf("%d ", chapas[ch - 1]);

    return 0;
}

/*
int main(int argc, char const *argv[]){
    int chapa, chapas[100000], llave, ch;

    scanf("%d", &chapa);
    for(int i = 0; i < chapa; i++)
        scanf("%d", &chapas[i]);
    scanf("%d", &llave);
    
    for (int i = 0; i < llave; i++)
        if(scanf("%d", &ch) == 1)
            for (int j = 0; j < chapa; j++)
                if(chapas[j] > ch || ch > chapas[chapa - 1] || ch < chapas[0]){
                    printf("0 ");
                    break;
                }
                else if(chapas[j] == ch){  
                    printf("%d ", j + 1);
                    break;
                }
                else if (chapas[(int) chapa / 2] < ch)
                    j = chapa / 2;


    return 0;
}
*/

/*int main(int argc, char **arg)
{
    int chapa, *chapas, llave, *llaves, *respuesta, ch;

    scanf("%d", &chapa);
    chapas = (int *) calloc(chapa, sizeof(int));
    getchar();
    
    for (int i = 0; i < chapa; i++)
        if((ch = getchar()) && (ch != ' '))
            chapas[i] = ch - '0';
        else
            i--;
    
    scanf("%d", &llave);
    llaves = (int *) malloc(llave * sizeof(int));
    getchar();

    for (int i = 0; i < llave; i++)
        if((ch = getchar()) && (ch != ' '))
            for (int j = 0; j < chapa; j++)
                if(chapas[j] == ch - '0'){  
                    llaves[i] = j + 1;
                    break;
                }
                else if(j == chapa - 1)
                    llaves[i] = 0;
                else
                    continue;
        else
            i--;

    for (int i = 0; i < llave; i++)
        printf("%d ", llaves[i]);
    printf("\n");
    
    return 0;
}*/
