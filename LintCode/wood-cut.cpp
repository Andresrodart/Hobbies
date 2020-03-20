#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
#define ll long long 
using namespace std;

class Solution {
public:
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    int woodCut(vector<int> &L, int k) {
        if(L.size() == 0) return 0;
        ll maxNum = *max_element(L.begin(), L.end()); 
        return (int) this->binary(k, L, 1, maxNum);
    }
    ll binary(ll k, vector<int> &L, ll minNum, ll maxNum){
        ll mid = (maxNum + minNum)/2;
        if(minNum > maxNum || mid == 0) return 0;
        ll res = 0;
        for(auto block: L) res += block/mid;
        if( res >= k) return max(mid, this->binary(k, L, mid + 1, maxNum));
        else return this->binary(k, L, minNum, mid - 1);
    }
};


int main(int argc, char const *argv[]){
    vector<int> a = {2147483644,2147483645,2147483646,2147483647};
    std::cout << Solution().woodCut(a, 4) << std::endl;
    return 0;
}
