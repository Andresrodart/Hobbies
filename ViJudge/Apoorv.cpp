#include <vector>
#include <iostream>
#include <algorithm> 
#include <unordered_map>
using namespace std;

class fenwick{
    private:
        vector<int> arr;
        int lenght;
    public:
    fenwick(int n);
    int add(int r);
    void update(int l, int delta);
};

fenwick::fenwick(int n){
    fenwick::arr = vector<int>(n, 0);
    fenwick::lenght = n;
}

int fenwick::add(int r){
    int res = 0;
    for (; r >= 0; r = (r & (r + 1)) - 1){
        res += fenwick::arr[r];
        cout << r << endl;
    }
    return res;
}

void fenwick::update(int l, int delta){
    for (;l < fenwick::lenght; l = l | (l + 1))
        fenwick::arr[l] += delta;
}

void coordinateCompression(vector<int> &arr){
    vector<int> aux(arr.begin(), arr.end());
    unordered_map<int, int> umap;
    sort(aux.begin(), aux.end());
    for (size_t i = 0, j = 0; i < arr.size(); i++){
        if(umap.find(aux[i]) == umap.end())
            umap[aux[i]] = j++;
        if(aux[i] == aux.back())
            break;
    }
    for (size_t i = 0; i < arr.size(); i++)
        arr[i] = umap[arr[i]];
}

int main(int argc, char const *argv[]){
    int n, p, x, res = 0, in = 0;
    cin >> n >> p;
    fenwick fnwick(n);
    vector<int> arr(n);
    for (size_t i = 0; i < n; i++)
        cin >> arr[i];
    coordinateCompression(arr);
    if(p > 1){
        for (size_t i = n - 1; i > n - p; i--){
            fnwick.update(arr[i], 1);
			res += fnwick.add(arr[i] - 1);
            cout << endl;    
        }
		int winRes = res;
        for(size_t i = n - p; i >= 0; i--){
            fnwick.update(arr[i + p], - 1);
			winRes += fnwick.add(arr[i] - 1) - fnwick.add(n - 1) + fnwick.add(arr[i + p]);
			fnwick.update(arr[i], 1);
			if (winRes > res){
				res = winRes;
				in = i;
            }
        }
    }
	cout << in + 1 << " " << res;
    return 0;
}
