#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

bool addCharDistance(string A, string B){
	size_t lenA = A.length(), lenB = B.length(), i = 0, j = 0, dif = 0;		// O(1)
	while(i < lenA && j < lenB){									        // O(A)
		if(dif > 1) return False;										    	// O(1)
		if(A[i] != B[j]){i++; dif++;}											// O(1)
		else{i++; j++;}															// O(1)
	}
	dif += lenA - i;														// O(1)
	return (dif <= 1)? True : False; 										// O(1)
}

bool changeCharDistance(string A, string B){
	size_t lenA = A.length(), lenB = B.length(), i = 0, j = 0, dif = 0;		// O(1)
	while(i < lenA && j < lenB)										        // O(N)
		if(dif > 1) return False;										    	// O(1)
		else if(A[i++] != B[j++]) dif++;										// O(1)
	return (dif <= 1)? True : False; 										// O(1)
}

bool oneAwaySimple(string A, string B){
	size_t lenA = A.length(), lenB = B.length(), i = 0, j = 0, dif = 0;		// O(1)
	while(i < lenA && j < lenB){									        // O(A)
		if(dif > 1) return False;										    	// O(1)
		if(A[i] != B[j])
			if(lenA > lenB){i++; dif++;}										// O(1)
			else{i++; j++; dif++;}												// O(1)
		else{i++; j++;}															// O(1)
	}
	dif += lenA - i;														// O(1)
	return (dif <= 1)? True : False; 										// O(1)
}

bool oneAway(string A, string B){
	size_t lenA = A.length(), lenB = B.length(), i = 0, j = 0;				// O(1)
	int dif = lenA - lenB;													// O(1)
	if(abs(dif) > 1) return False;											// O(1)
	else if(dif < 0) return oneAwaySimple(B, A);							// O(N) N = maxLength(lenA, lenB)
	return oneAwaySimple(A, B);												// O(N) N = maxLength(lenA, lenB)
	// if(dif == 0) return changeCharDistance(A, B);						// O(N)
	// else if(dif < 0) return addCharDistance(B, A)						// O(N) N = maxLength(lenA, lenB)
	// return addCharDistance(A, B);										// O(N) N = maxLength(lenA, lenB)
}

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(false);
	string s = "aDb";
	string t = "adb";
	cout << oneAway(s, t) << "\n";
	cout << oneAway("bcde", "abcde") << "\n";
	cout << oneAway("pale", "ple") << "\n";
	cout << oneAway("pales", "pale") << "\n";
	cout << oneAway("pale", "bale") << "\n";
	cout << oneAway("pale", "bake") << "\n";
	cout << oneAway("pal", "palee") << "\n";
	return 0;
}