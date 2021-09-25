#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

long long int SUMS[1000000];

bool fitsInStorage(vector<long long int> arry, long long int arrySize, long long int maxSize, long long int nItems){
    for (long long int idx = 0; idx <= arrySize - nItems; idx++) {
		if (SUMS[idx + nItems - 1] - SUMS[idx - 1] > maxSize)
			return False;
    }
	return True;
}

long long int searchMaxR(vector<long long int> arry, long long int arrySize, long long int maxSize){
    long long int L = 0 , R = arrySize, mid;
	long long int ans = 0;
	while (L <= R){
		mid = (L + R) / 2;
		if(fitsInStorage(arry, arrySize, maxSize, mid)){
			L = mid + 1;
			ans = mid;
		}
		else
			R = mid - 1;
	}
	return ans;
}
	
vector<long long int> readArray(long long int size){
    long long int aux;
    vector<long long int> arry;
    while (--size)
    {
		cin >> aux;
		arry.push_back(aux);
	}
	return arry;
}
void printArry(vector<long long int> arr){
    for(auto a: arr)
        cout << a << ' ';
}

long long int searchMinL(vector<long long int> arry, long long int arrySize, long long int maxSize, long long int RElements){
	for (long long int idx = 0; idx <= arrySize - RElements; idx++) {
		if (
			SUMS[idx + RElements - 1] - SUMS[idx - 1] > maxSize

		)
			return idx + 1;
	}
	return -1;
}

long long int toInt(string str){
    str.pop_back();
    long long int num; 
    stringstream ss;  
    ss << str;  
    ss >> num; 
    return num;
}

void makeSums(vector<long long int> arr, int arrSize){
	long long int sum = 0;
    for (long long int i = 0; i < arrSize; i++) {
        sum += arr[i];
		SUMS[i] = sum;
	}
}

int main( int argc, char const *argv[]){
	std::ios_base::sync_with_stdio(False);
    long long int N, R = 0, L = -1, maxSize;
    string C;
    vector <long long int> sizes;
	std::cin >> N >> C;
	sizes = readArray(N + 1);
	long long int lastChar = C.size() - 1;
	if(C[lastChar] == 'M') maxSize = toInt(C);
	else if(C[lastChar] == 'G') maxSize = toInt(C) * 1024;
	else if(C[lastChar] == 'T') maxSize = toInt(C) * 1024 * 1024;
	makeSums(sizes, N);
	R = searchMaxR(sizes, N, maxSize);
	L = searchMinL(sizes, N, maxSize, R + 1);
    std::cout << R << ' ' << L;	
	return 0;
}
