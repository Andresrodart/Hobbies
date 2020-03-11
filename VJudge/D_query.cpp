//#include <vector>
#include <stdio.h>
//#include <algorithm>
//#include <iostream>
//#include <climits>
#define ll long long 
using namespace std;
const ll MAXN = 100000;
ll log__2[MAXN + 1];
class initLog2{	
	public:
		initLog2(){
			log__2[1] = 0;
			for (int i = 2; i <= MAXN; i++)
				log__2[i] = log__2[i/2] + 1;
		}
};
initLog2 init;
const ll k = log__2[MAXN] + 1;
ll SaparTree[MAXN][18][3];
ll arr[MAXN];
int max(ll a, ll b){
	return (a > b)? a:b;
}
ll queryST(int L, int R){
	ll j = log__2[R - L + 1];
	ll resA = SaparTree[L][j][1];
	ll al = SaparTree[L][j][0];
	ll ar = SaparTree[L][j][2];
	ll resB = SaparTree[R - (1 << j) + 1][j][1];
	ll bl = SaparTree[R - (1 << j) + 1][j][0];
	ll br = SaparTree[R - (1 << j) + 1][j][2];
	if (arr[L + (1 << j) - 1] == arr[R - (1 << j) + 1] and L != R)
			return max(resA, max(resB, ar + bl - (L - R + 2*(1 << j) - 1)));
	return max(resA, resB);
}

void buildST(ll length){
	for (size_t i = 0; i < length; i++)
		SaparTree[i][0][0] = 1, SaparTree[i][0][1] = 1, SaparTree[i][0][2] = 1;
	for(int j = 1; j < k; j++)
		for(int i = 0; i + (1 << j) <= length; i++){
			int a = SaparTree[i][j - 1][1],
				al = SaparTree[i][j - 1][0],
				ar = SaparTree[i][j - 1][2];
			int b = SaparTree[i + (1 << (j - 1))][j - 1][1],
				bl = SaparTree[i + (1 << (j - 1))][j - 1][0],
				br = SaparTree[i + (1 << (j - 1))][j - 1][2];
			if(arr[i + (1 << (j - 1)) - 1] != arr[i + (1 << (j - 1))]){
					SaparTree[i][j][1] = a++, 
					SaparTree[i][j][0] = al, 
					SaparTree[i][j][2] = br;
			}
			else{
				SaparTree[i][j][1] = max(a, b), 
				SaparTree[i][j][0] = al, 
				SaparTree[i][j][2] = br;
			}
		}
}


int main(int argc, char const *argv[]){
	ll tests = 1, n, querys, element, rigt, lef;
 	scanf("%lld",&tests);
 	while (tests != 0){
 		n = tests;
 		scanf("%lld", &querys);
		for (int i = 0; i < n; i++)
			scanf("%lld", arr + i);	
		buildST(n);
 		while (querys--){
 			scanf("%lld %lld", &lef, &rigt);
 			printf("%lld\n", queryST(lef - 1, rigt - 1));
 		}
 		scanf("%lld", &tests);
 	}
	return 0;
}