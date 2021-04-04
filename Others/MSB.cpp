#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h> 
#include <curses.h>

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

int main(int argc, char const *argv[]){
    cout << setBitNumber(8) << endl;
    cout << setBitNumber(5) << endl;
    cout << setBitNumber(7) << endl;
    cout << setBitNumber(3) << endl;
    return 0;
}
