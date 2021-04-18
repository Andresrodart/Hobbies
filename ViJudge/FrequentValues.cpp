#include <vector>
//#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <climits>
#define ll long long 
using namespace std;
const unsigned int MAXN = 100000;
ll log__2[MAXN + 1];
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

class SparseTable{
	private:
		vector<ll> arr, arrR;
		ll length, k, **ST, **STr;
	public:
	SparseTable(vector<ll> arr, ll length){
		this -> arr = arr;
		this -> length = length;
		this -> k = log__2[MAXN] + 1;
		this -> ST = (ll **) malloc(MAXN * sizeof(ll *));
		for (size_t i = 0; i < MAXN; i++)
			this -> ST[i] = (ll *) malloc((this -> k + 1) * sizeof(ll));
		build();
	}
	void build();
	int query(int L, int R);
};
void SparseTable::build(){
	for (size_t i = 0; i < this->length; i++)
		this->ST[i][0] = 1;
	for(int j = 1; j < this->k; j++)
		for(int i = 0; i + (1 << j) <= this->length; i++){
			int a = this->ST[i][j - 1];
			int b = this->ST[i + (1 << (j - 1))][j - 1];
			this->ST[i][j] = (this->arr[i + (1 << (j - 1)) - 1] == this->arr[i + (1 << (j - 1))]) ? (a + b):max(a, b);
		}
}
int SparseTable::query(int L, int R){
	ll j = log__2[R - L + 1];
	ll resA = this->ST[L][j];
	ll resB = this->ST[R - (1 << j) + 1][j];
	if (resA == resB && resA == (1 << j))
		return resA + resB - (L - R + 2 * (1 << j) - 1);
	return max(resA, resB);
}

int main(int argc, char const *argv[]){
	ll tests = 1, n, querys, element, rigt, lef, res, cont = 1, aux, j = 0;
	log__2[1] = 0;
	for (int i = 2; i <= MAXN; i++)
    	log__2[i] = log__2[i/2] + 1;
 	cin >> tests;
 	while (tests != 0){
 		n = tests;
 		cin >> querys;
 		vector<ll> arr;
        for (int i = 0; i < n; i++){
 			cin >> element;
 			arr.push_back(element);
 		}
		SparseTable ST{arr, n};
 		while (querys--){
 			cin >> lef >> rigt;
 			res = LLONG_MIN;
 			std::cout << ST.query(lef - 1, rigt - 1) << std::endl;
 		}
 		cin >> tests;
 	}
	return 0;
}

// #include <utility>
// #include <vector>
// #include <iostream>
// #include <algorithm>
// #include <climits>
// #define ll long long 
// using namespace std;

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