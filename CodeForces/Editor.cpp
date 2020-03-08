#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#define ll long long
using namespace std;
class fenwick{
    private:
        vector<ll> arr;
        ll lent;
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
    fenwick::lent = n + 1;
}
fenwick::fenwick(vector<ll> arr, size_t n){
    fenwick::arr = vector<ll>(n + 1, 0);
    fenwick::lent = n + 1;
	for (size_t i = 0; i < n; i++)
		fenwick::update(i, arr[i]);
	
}
int fenwick::size(){return lent;}
ll fenwick::add(ll r){
    ll res = 0;
    for (; r >= 0; r = (r & (r + 1)) - 1)
        res += fenwick::arr[r];
    return res;
}
int main(int argc, char const *argv[]){
    ll n, l = 0, r = 0, j = 0;
    string query;
    cin >> n;
    cin >>  query;
    vector<int> left(query.size());
    vector<int> right(query.size());
    stack<int> stc;
    fenwick fn(query.size());
    for (size_t i = 0; i < query.size(); i++){
        if (query[i] == '(')
            l++;
        else if (query[i] == ')')
            r++;
        else if (query[i] == 'L' && j > 0){
            j--;
            l = left[j];
            r = right[j];
        }
        else if (query[i] == 'R')
            j++;
        left[j] = l;
        right[j] = r;
        if(left[j] - left[i] == 0){
            fn.update(j, 1);
            cout << fn.add(j) << " ";
        }else cout << -1 << " ";
    }
    
    return 0;
}
