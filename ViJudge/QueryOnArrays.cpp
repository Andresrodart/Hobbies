#include <set>
#include <vector>
#include <iostream>
#include <algorithm> 
using namespace std;
#define ll long long

class fenwick{
    private:
        vector<ll> arr;
        ll lenght;
    public:
    fenwick(ll n);
    fenwick(vector<ll> arr, size_t n);
    void update(ll l, ll delta);
    void replace(ll l, ll delta);
	ll add(ll r);
    int size();
};
fenwick::fenwick(ll n){
    fenwick::arr = vector<ll>(n + 1, 0);
    fenwick::lenght = n + 1;
}
fenwick::fenwick(vector<ll> arr, size_t n){
    fenwick::arr = vector<ll>(n + 1, 0);
    fenwick::lenght = n + 1;
	for (size_t i = 0; i < n; i++)
		fenwick::update(i, arr[i]);
	
}
int fenwick::size(){return lenght;}
ll fenwick::add(ll r){
    ll res = 0;
    for (; r >= 0; r = (r & (r + 1)) - 1)
        res += fenwick::arr[r];
    return res;
}

void fenwick::replace(ll l, ll delta){
	ll pos = l;
	ll prevDelta = fenwick::add(l) - fenwick::add(l - 1);
    for (;pos < fenwick::lenght; pos = pos | (pos + 1))
        fenwick::arr[pos] -= prevDelta;
	fenwick::update(l, delta);
}

void fenwick::update(ll l, ll delta){
    for (;l < fenwick::lenght; l = l | (l + 1))
        fenwick::arr[l] += delta;
}

int main(int argc, char const *argv[]){
    ll n, q = 0, option, delta;
	cin >> n;
    vector<ll> arr(n);
	for (ll i = 0; i < n; i++)
        cin >> arr[i];
    cin >> q;
	fenwick fnwick(arr, n);
	
	while (q > 0){
		cin >> option;
		if (option == 2){
			set<int> st = {0};
		    string res = "NO";
			cin >> delta;
			for (size_t i = 0; i < n; i++){
				ll aux = fnwick.add(i);
				if (st.find(aux - delta) != st.end()){
					res = "YES";
					break;
				}else st.insert(aux);
			}
			std::cout << res << "\n";
		}else{
			cin >> option >> delta;
			fnwick.replace(option - 1, delta);
		}
		q--;
	}
	
    return 0;
}
