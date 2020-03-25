#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;
// HT = HastTable

bool PalindromePermutation(string str){ 		                        // Just for ascii strings
	transform(str.begin(), str.end(), str.begin(), ::tolower);          // O(n)
	str.erase(remove(str.begin(), str.end(), ' '),str.end());			// O(n)
	unordered_map<char, size_t> HT;			                            // O(1)
	size_t impair = 0;                     								// O(1)
	for(auto chr : str)						        // O(n)
		if(HT.find(chr) != HT.end()) HT[chr] +=1;	// O(1)
		else HT[chr] = 1;       					// O(1)
	for(auto duple: HT)						// O(n)
		if(duple.second & 1) impair++;
		if(impair > 1) return False;
	return True;
}
int main(int argc, char const *argv[]){
	cout << PalindromePermutation("Hello world!") << '\n';
	cout << PalindromePermutation("Tact Coa") << '\n';
	cout << PalindromePermutation("carerac") << '\n';
	cout << PalindromePermutation("aa") << '\n';
	cout << PalindromePermutation("accba") << '\n';
	cout << PalindromePermutation("asccba") << '\n';
	return 0;
}