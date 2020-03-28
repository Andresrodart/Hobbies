#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
#if !defined(None)
#define None  NULL
#endif
using namespace std;
typedef vector<char> vc;

void pushDigits(vc &str, size_t integer){
	string res, digits;							// O(1)
	ostringstream os;							// O(1)
	os << integer;								// O(1)
	digits = os.str();							// O(1) <- Max number handle by unsigned int
	for(auto chr:digits) str.push_back(chr);	// O(1) <- Max number handle by unsigned int
}

string stringCompression(string str){
	vc newString;                               // O(1)
	char auxChar = 1;                           // O(1)
	size_t count = 1;							// O(1)
	for(char chr: str)							// O(n)
		if(auxChar == 1) auxChar = chr;				// O(1)	
		else if(chr != auxChar){					// O(1)
			newString.push_back(auxChar);				// O(1)
			pushDigits(newString, count);				// O(1)
			auxChar = chr;								// O(1)
			count =  1;									// O(1)
		}else count++;								// O(1)
	newString.push_back(auxChar);			// O(1)
	pushDigits(newString, count);			// O(1)
	string res (newString.begin(), newString.end());
	return (res.length() >= str.length())? str : res;	// O(1)
}

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(False);
	cout << stringCompression("aabcccccaaa") << std::endl;		
	cout << stringCompression("abbbbbbbbbbbb") << std::endl;		
	return 0;
}