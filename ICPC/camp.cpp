#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

long long int bs(long long int number, long long int max_difficulty, vector<int> &p){
	long long int l  = 0, r = p.size() - 1, pos = 0, aux;
	while (l < r){
		long long int mid = (l + r) / 2;
		if (p[mid] + number <= max_difficulty)
			pos = mid, l = mid + 1;
		else r = mid - 1;

	}
	if (pos < 0 || pos > p.size() || p[pos] + number > max_difficulty) return INT_MAX;
	aux = p[pos];
	p.erase(p.begin() + pos);
	return abs(aux - number);
}

long long int solve(vector<int> p, vector<int> q, long long int n, long long int s){
	long long int res = 0;
	for (long long int i = index + n - 1; i >= index; i--){
		n = q[i];
		res = max(res, bs(n, s, p));
	}
	return res;
}


int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(False);
	vector<int> p_arry;
	vector<int> q_arry;
	vector<int> aux_arry;
	long long int res = INT_MAX;
	long long int n, p, q, s, aux;
	cin >> n >> p >> q >> s;	
	while(p--){
		cin >> aux;
		p_arry.push_back(aux);
	}
	sort(p_arry.begin(), p_arry.end()); 
	while (q--){
		cin >> aux;
		q_arry.push_back(aux);
	}
	sort(q_arry.begin(), q_arry.end()); 
	
	res = solve(p_arry, q_arry, n, s);
	cout << ((res <= s) ? res : -1);
	return 0;
}