#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

bool addSpace(string &mString, int64_t &j){
	mString[j--] = '0';		    // O(1)
	mString[j--] = '2';			// O(1)
	mString[j--] = '%';			// O(1) <-- here j can go to be -1
	return True;
}

void URLify(string &mString, size_t realLength){
	int64_t i = realLength - 1, j = mString.length() - 1;		// O(1)
	while(i <= j && j > 0)										// O(n)
		if(mString[i] != ' ') swap(mString[i--], mString[j--]); 			// O(1)
		else if(mString[i] == ' ' && mString[j] == ' ')             		// O(1)
			if(addSpace(mString, j)) while(i > 0 && mString[i] == ' ')i--;	// O(n)
}

int main(int argc, char const *argv[]){
	string example = "no thing  ";
	vector<pair<string, size_t> > strings = {
		{"Mr John Smith    ", 13},
		{"Mr John Smith      ", 14},
		{"MrJohnSmith", 11},
		{" Mr John    ", 8},
		{"   ", 1},
		{"", 0}
	};
	for(auto &pair: strings)
		URLify(pair.first, pair.second);
	for(auto &pair: strings)
		cout << pair.first << endl;
	return 0;
}