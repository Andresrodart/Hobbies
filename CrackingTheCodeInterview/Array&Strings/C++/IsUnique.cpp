#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif 
#if !defined(False)
#define False (!True)
#endif
using namespace std;

// Is necessary to start the iteration from 1 and not in zero, because if string is empty the size - 1 is negative
bool isUnique(string str){
	sort(str.begin(), str.end()); 						// O(n log(n))
	for(size_t i = 1; i < str.length(); i++)			// O(n)
		if (str[i] == str[i - 1]) return False;			// O(1)
	return True;
}

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(false);
	std::cout << isUnique("sdadsa") << std::endl <<
	isUnique("") << std::endl << 
	isUnique("asdfghjk") << std::endl <<
	isUnique("asdffghjklzz") << std::endl;
	return 0;
}
