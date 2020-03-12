#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h> 

#define ll long long 
using namespace std;

int setBitNumber(int n){ 
    // To find the position 
    // of the most significant 
    // set bit 
    int k = (int)(log2(n)); 
  
    // To return the the value 
    // of the number with set 
    // bit at k-th position 
    return (int)(pow(2, k)); 
} 
  

ll piles[1001];
int main(){
    ll n;
    scanf("%lld", &n);
    while(n != 0){
        ll colsOfOnes = 0, count = 0;
        for(ll i = 0; i < n; i++)
        scanf("%lld", piles + i);
        for(ll i = 0; i < n; i++)
            colsOfOnes ^= piles[i];
        colsOfOnes = setBitNumber(colsOfOnes);
        if(colsOfOnes != 0)
            for(ll i = 0; i < n; i++)
                if((piles[i] & colsOfOnes) != 0)
                    count++;  
        printf("%lld\n", count);
        scanf("%lld", &n);
  }
  return 0;
}