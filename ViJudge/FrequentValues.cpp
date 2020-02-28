#include <utility>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#define ll long long 
using namespace std;

int main(int argc, char const *argv[]){
	ll tests = 1, n, querys, element, rigt, lef, res, cont = 1, aux, j = 0;
	cin >> tests;
	while (tests != 0){
		n = tests;
		cin >> querys;
		vector<pair<ll, ll>> arr;
        cin >> element;
        aux = element;
        arr.push_back(make_pair(j, cont++));
		for (int i = 1; i < n; i++){
			cin >> element;
			if (element != aux){
                j = i;
				cont = 1;
				aux = element;
            }
			arr.push_back(make_pair(j, cont++));
		}
		while (querys--){
			cin >> lef >> rigt;
			res = LLONG_MIN;
			lef--;
			rigt--;
			while (lef <= rigt){
				res = (lef < arr[rigt].first)? max(res, arr[rigt].second):max(res, arr[rigt].second - arr[rigt - 1].second);
				rigt = arr[rigt].first - 1;
			}
			std::cout << res << std::endl;
		}
		cin >> tests;
	}
	
	return 0;
}