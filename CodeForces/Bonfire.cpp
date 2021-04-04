#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(False);
	uint64_t n, x, k, aux, prev;
    x = 0;
	cin >> n;
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	vector<string> arr(n);
	for(uint64_t i = 0; i < n; i++){
	    cin >> arr[i];
        x += arr[i].size();
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    }
	cin >> k;
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    aux = (k / x);
    k -= (k / x) * x;
    // cout << x << " - " << k << endl;
    while (True){
        string name = arr[aux++ % n];
        if(name.size() < k) {
            k -= name.size();
            continue;
        }
        else{
            cout << name[k - 1];
            break;
        }
    }

	return 0;
}