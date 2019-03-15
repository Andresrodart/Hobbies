#include <iostream>

void insertionSort(int *arr, int n){
    int key, j; 
    for (int i = 1; i < n; i++) { 
        key = arr[i]; 
        j = i-1; 
        while (j >= 0 && arr[j] > key){ 
           arr[j+1] = arr[j]; 
           j = j-1; 
       } 
       arr[++j] = key; 
   } 
}
 
int main(int argc, char const *argv[])
{
    int a[3],z[3];
    std::cin >> a[0] >> a[1] >> a[2] >> z[0] >> z[1] >> z[2];
    insertionSort(a, 3);
    insertionSort(z, 3);
    if(a[0] <= z[0] && a[1] <=  z[1] && a[2] <= z[2])
        std::cout << '1';
    else
        std::cout << '0';
 
    return 0;
}
