#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

//  BS = Better space, BT = Better time
bool checkPermutationBS(string A, string B){
	// transform(A.begin(), A.end(), A.begin(), ::tolower); if case sensitive not needed
	// transform(B.begin(), B.end(), B.begin(), ::tolower); if case sensitive not needed
	size_t lenA = A.length(), lenB = B.length();			// O(1)
	if(lenA != lenB) return False;							// O(1)
	sort(A.begin(), A.end());                               // O(n log(n))
	sort(B.begin(), B.end());                               // O(n log(n))
	for(size_t i = 0; i < lenA; i++)						// O(n)
		if (A[i] != B[i]) return False;						// O(1)
	return True;
}
bool checkPermutationBT(string A, string B){
	// transform(A.begin(), A.end(), A.begin(), ::tolower); if case sensitive not needed
	// transform(B.begin(), B.end(), B.begin(), ::tolower); if case sensitive not needed
	size_t lenA = A.length(), lenB = B.length();			// O(1)
	if(lenA != lenB) return False;							// O(1)
	unordered_map<char, size_t> hashTable;					// O(1)
	for(auto chr: A)										// O(n)
		if(hashTable.find(chr) != hashTable.end()) hashTable[chr]++;	// O(1)
		else hashTable[chr] = 1;                       					// O(1)
	for(auto chr: B)										// O(n)
		if(hashTable.find(chr) == hashTable.end()) return False;		// O(1)
		else hashTable[chr] -= 1;                  						// O(1)
	for(auto duple: hashTable)								// O(n)
		if(duple.second != 0) return False;								// O(1)
	return True;
}

int main(int argc, char const *argv[]){
	std::cout << checkPermutationBS("asdfg", "gasfd") << checkPermutationBT("asdfg", "gasfd") << std::endl;
	std::cout << checkPermutationBS("asdf", "addf") << checkPermutationBT("asdf", "addf") << std::endl;
	std::cout << checkPermutationBS("", "") << checkPermutationBT("", "") << std::endl;
	std::cout << checkPermutationBS("", "qwer") << checkPermutationBT("", "qwer") << std::endl;
	std::cout << checkPermutationBS("CAT", "ACT") << checkPermutationBT("CAT", "ACT") << std::endl;    
	return 0;
}