#include <vector>
//#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <climits>
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
ll SaparTree[MAXN][17][3];
vector<ll> arr;

int queryST(int L, int R){
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
			if(arr[i + (1 << (j - 1)) - 1] == arr[i + (1 << (j - 1))]){
				if(arr[i] == arr[i + 2*(1 << (j - 1))- 1]){
					SaparTree[i][j][1] = (a + b);
					SaparTree[i][j][0] = (a + b); 
					SaparTree[i][j][2] = (a + b);
				}
				else if(arr[i] == arr[i + (1 << (j - 1))]){
					SaparTree[i][j][1] = max(b, a + bl); 
					SaparTree[i][j][0] = (al + bl);
					SaparTree[i][j][2] = br;
				}
				else if(arr[i + (1 << (j - 1))] == arr[i + (1 << (j - 1)) + j - 1]){
					SaparTree[i][j][1] = max(a, b + ar),
					SaparTree[i][j][0] = al, 
					SaparTree[i][j][2] = (br + ar);
				}
				else{
					SaparTree[i][j][1] = max(a, max(b, ar + bl)), 
					SaparTree[i][j][0] = al, 
					SaparTree[i][j][2] = br;
				}
			}
			else{
				SaparTree[i][j][1] = max(a, b), 
				SaparTree[i][j][0] = al, 
				SaparTree[i][j][2] = br;
			}
		}
}


//SparseTable ST{};
int main(int argc, char const *argv[]){
	ll tests = 1, n, querys, element, rigt, lef;
 	cin >> tests;
 	while (tests != 0){
 		n = tests;
 		cin >> querys;
		arr = {};
        for (int i = 0; i < n; i++){
 			cin >> element;
 			arr.push_back(element);
 		}
		//ST.setArr(arr, n);
		buildST(n);
 		while (querys--){
 			cin >> lef >> rigt;
 			std::cout << queryST(lef - 1, rigt - 1) << std::endl;
 		}
 		cin >> tests;
 	}
	return 0;
}
/*class SparseTable{
	private:
		vector<ll> arr, arrR;
		ll length, k, ***ST;
	public:
		SparseTable(vector<ll> arr, ll length){
			this -> arr = arr;
			this -> length = length;
			this -> k = log__2[MAXN] + 1;
			this -> ST = (ll ***) malloc(MAXN * sizeof(ll **));
			for (size_t i = 0; i < MAXN; i++){
				this -> ST[i] = (ll **) malloc((this -> k + 1) * sizeof(ll *));
				for (size_t j = 0; j < this -> k + 1; j++)
					this -> ST[i][j] = (ll *) malloc(3 * sizeof(ll));
				
			}
			this->build();
		}
		SparseTable(){
			this -> k = log__2[MAXN] + 1;
			this -> ST = (ll ***) malloc(MAXN * sizeof(ll **));
			for (size_t i = 0; i < MAXN; i++){
				this -> ST[i] = (ll **) malloc((this->k + 1) * sizeof(ll *));
				for (size_t j = 0; j < this -> k + 1; j++)
					this -> ST[i][j] = (ll *) malloc(3 * sizeof(ll));
				
			}
		}
		void build();
		int query(int L, int R);
		void setArr(vector<ll> arr, ll length);
};
	
void SparseTable::setArr(vector<ll> arr, ll length){
	this -> arr = arr;
	this -> length = length;
	this -> build();
}
void SparseTable::build(){
	for (size_t i = 0; i < this->length; i++)
		this->ST[i][0][0] = 1, this->ST[i][0][1] = 1, this->ST[i][0][2] = 1;
	for(int j = 1; j < this->k; j++)
		for(int i = 0; i + (1 << j) <= this->length; i++){
			int a = this->ST[i][j - 1][1],
				al = this->ST[i][j - 1][0],
				ar = this->ST[i][j - 1][2];
			int b = this->ST[i + (1 << (j - 1))][j - 1][1],
				bl = this->ST[i + (1 << (j - 1))][j - 1][0],
				br = this->ST[i + (1 << (j - 1))][j - 1][2];
			if(this->arr[i + (1 << (j - 1)) - 1] == this->arr[i + (1 << (j - 1))]){
				if(this->arr[i] == this->arr[i + (1 << (j - 1)) + j - 1]){
					this->ST[i][j][1] = (a + b);
					this->ST[i][j][0] = (a + b); 
					this->ST[i][j][2] = (a + b);
				}
				else if(this->arr[i] == this->arr[i + (1 << (j - 1))]){
					this->ST[i][j][1] = max(b, a + bl); 
					this->ST[i][j][0] = (al + bl);
					this->ST[i][j][2] = br;
				}
				else if(this->arr[i + (1 << (j - 1))] == this->arr[i + (1 << (j - 1)) + j - 1]){
					this->ST[i][j][1] = max(a, b + ar),
					this->ST[i][j][0] = al, 
					this->ST[i][j][2] = (br + ar);
				}
				else{
					this->ST[i][j][1] = max(a, max(b, ar + bl)), 
					this->ST[i][j][0] = al, 
					this->ST[i][j][2] = br;
				}
			}
			else{
				this->ST[i][j][1] = max(a, b), 
				this->ST[i][j][0] = al, 
				this->ST[i][j][2] = br;
			}
		}
}
int SparseTable::query(int L, int R){
	ll j = log__2[R - L + 1];
	ll resA = this->ST[L][j][1];
	ll resB = this->ST[R - (1 << j) + 1][j][1];
	if (resA == resB && resA == j && L != R - (1 << j) + 1)
		return resA + resB - (L - R + 2 * (1 << j) - 1);
	return max(resA, resB);
}*/
// ll arr[MAXN];
// class SegmentTree{
// 	//private:
// 	public:
// 		ll ST[2 * MAXN][3], length;
// 	//public:
// 		SegmentTree(ll length, ll val){
// 			this -> length = length;
// 			arrOfOneVal(val);
// 		}
// 		void build(/*ll (*f)(ll lChild, ll rChild)*/);
// 		void arrOfOneVal(ll val);
// 		void setVal(ll i, ll val);
// 		ll query(ll l, ll r) 
// };
// void SegmentTree::build(){
// 	/*after adding the array at the end of ST in ST[1..n) 
// 	are empty and ST[n..2n) have the original array AKA leaves */
// 	ll leftSonEnd = 0;
// 	for (int i = this->length - 1; i > 0; --i){
// 	/*now we make roots from bottom to top*/
// 		if(this->ST[i<<1][2] == this->ST[i<<1|1][0])
// 			this->ST[i][1] = this->ST[i<<1][1] + this->ST[i<<1|1][1];
// 		else
// 			this->ST[i][1] = max(this->ST[i<<1][1], this->ST[i<<1|1][1]);
// 		this->ST[i][0] = this->ST[i<<1][0];
// 		this->ST[i][2] = this->ST[i<<1|1][2];
// 	}
// }
// void SegmentTree::arrOfOneVal(ll val){
// 	for(size_t i = this->length; i < 2 * this->length; i++)
// 		this->ST[i][1] = 1;
// }
// // void SegmentTree::setVal(ll i, ll val){
// // 	this->ST[i] = val;
// // }

// ll SegmentTree::query(ll l, ll r) {  // sum on interval [l, r)
//   int res = 0;
//   for (l += this->length, r += this->length; l < r; l >>= 1, r >>= 1) {
//     if (l&1) res += this->ST[l++];
//     if (r&1) res += this->ST[--r];
//   }
//   return res;
// }
// int main(int argc, char const *argv[]){
// 	ll tests = 1, n, querys, element, rigt, lef, res, cont = 1, aux, j = 0;
// 	scanf("%d", tests);
//   	while (tests != 0){
//   		n = tests;
//   		scanf("%d", querys);
//  		SegmentTree ST{n, 1};
//   		for (int i = 0; i < n; i++){
//   			scanf("%d", element);
// 			ST.ST[n + i][0] = element;
// 			ST.ST[n + i][2] = element;
// 		}
// 		ST.build();
//   		while (querys--){
//   			scanf("%d %d", lef, rigt);
//   			res = LLONG_MIN;
//   			std::cout << ST.query(lef - 1, rigt - 1) << std::endl;
//   		}
//   		cin >> tests;
//   	}
// 	return 0;
// }

// int main(int argc, char const *argv[]){
// 	ll tests = 1, n, querys, element, rigt, lef, res, cont = 1, aux, j = 0;
// 	cin >> tests;
// 	while (tests != 0){
// 		n = tests;
// 		cin >> querys;
// 		vector<pair<ll, ll>> arr;
//         cin >> element;
//         aux = element;
//         arr.push_back(make_pair(j, cont++));
// 		for (int i = 1; i < n; i++){
// 			cin >> element;
// 			if (element != aux){
//                 j = i;
// 				cont = 1;
// 				aux = element;
//             }
// 			arr.push_back(make_pair(j, cont++));
// 		}
// 		while (querys--){
// 			cin >> lef >> rigt;
// 			res = LLONG_MIN;
// 			lef--;
// 			rigt--;
// 			while (lef <= rigt){
// 				res = (lef < arr[rigt].first)? max(res, arr[rigt].second):max(res, arr[rigt].second - arr[rigt - 1].second);
// 				rigt = arr[rigt].first - 1;
// 			}
// 			std::cout << res << std::endl;
// 		}
// 		cin >> tests;
// 	}
	
// 	return 0;
// }
