#include <bits/stdc++.h>

#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

using namespace std;

bool isSubstring(string s1, string s2){
	s2 =  s2 + s2;
	if( s2.find(s1) != string::npos) return True;
	else return False;
}

int main(int argc, char const **argv){
	std::cout << isSubstring("waterbottle", "erbottlewat") << std::endl;
	std::cout << isSubstring("waterbottle", "erbottlewa") << std::endl;
	return 0;
}