#include <vector>
#include <iostream>
#include <algorithm> 
#include <unordered_map>
using namespace std;
#define ll long long

class fenwick{
    private:
        vector<ll> arr;
        ll lenght;
    public:
    fenwick(ll n);
    ll add(ll r);
    void update(ll l, ll delta);
};

fenwick::fenwick(ll n){
    fenwick::arr = vector<ll>(n + 1, 0);
    fenwick::lenght = n + 1;
}

ll fenwick::add(ll r){
    ll res = 0;
    for (; r >= 0; r = (r & (r + 1)) - 1)
        res += fenwick::arr[r];
    return res;
}

void fenwick::update(ll l, ll delta){
    for (;l < fenwick::lenght; l = l | (l + 1))
        fenwick::arr[l] += delta;
}

void coordinateCompression(vector<ll> &arr){
    vector<ll> aux(arr.begin(), arr.end());
    unordered_map<ll, ll> umap;
    sort(aux.begin(), aux.end());
    for (size_t i = 0, j = 1; i < arr.size(); i++){
        if(umap.find(aux[i]) == umap.end())
            umap[aux[i]] = j++;
        if(aux[i] == aux.back())
            break;
    }
    for (size_t i = 0; i < arr.size(); i++)
        arr[i] = umap[arr[i]];
}

int main(int argc, char const *argv[]){
    ll n, p, res = 0, in = 0, winRes = 0;
    cin >> n >> p;
    fenwick fnwick(n);
    vector<ll> arr(n);
    for (ll i = 0; i < n; i++)
        cin >> arr[i];
    coordinateCompression(arr);
	for (ll i = n - 1; i >= n - p; i--){
		fnwick.update(arr[i], 1);
		res += fnwick.add(arr[i] - 1);
	}
	winRes = res;
	in = n - p;
	for(ll i = n - p - 1; i >= 0; i--){
		fnwick.update(arr[i + p], - 1);
		winRes += fnwick.add(arr[i] - 1) - fnwick.add(n) + fnwick.add(arr[i + p]);
		fnwick.update(arr[i], 1);
		if (winRes >= res){
			res = winRes;
			in = i;
		}
	}
	std::cout << in + 1 << " " << res;
    return 0;
}
