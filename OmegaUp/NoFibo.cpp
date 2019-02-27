#include <stdio.h>

int main(int argc,char **arg){
    int fibo = 3, a = 1, b = 2, val;
    scanf("%d", &val);
    for(int i = 3;i < val; i++){
        if (i == fibo){
            a = b;
            b = fibo;
            fibo = a + b;
        }else
            printf("%d ", i);
    }
    return 0;
}