#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

bool smaller(std::string a, std::string b){
	if(a.size() == 0) return False;
	else if(b.size() == 0) return True;
	else if(a.size() == b.size()) return std::lexicographical_compare(a.begin(), a.end(), b.begin(), b.end());
	return a.size() < b.size();
}

std::string solve(std::string u, std::unordered_map< std::string, std::string > &nodes){
	u = nodes[u];
	return u;
}

int main(int argc, char const *argv[]){
	std::ios_base::sync_with_stdio(False);
	uintmax_t N;
	std::string u, v, x, little;
	std::cin >> N;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	std::unordered_map< std::string, std::string > nodes;
	while (N--){
		std::cin >> u >> v;
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		x = (nodes[u].size() > nodes[v].size())? nodes[u] : nodes[v];
		little = smaller(u, v)? (smaller(u, x)? u:x) : (smaller(v, x)? v:x);
		nodes[x] = little;
		nodes[u] = little;
		nodes[v] = little;
	}

	std::string message;
	std::getline(std::cin, message);
	std::istringstream ss(message);
    std::string word; // for storing each word
	ss >> word;
	if (nodes[word].size() > 0) std::cout << solve(word, nodes);
	else std::cout << word;
    while (ss >> word){
		if (nodes[word].size() > 0) std::cout << " " << solve(word, nodes);
		else std::cout << " " << word;
    }
	std::cout << std::endl;
	return 0;
}
// 8
// sea see
// see c
// you u
// and an
// n an
// are r
// ok k
// k z
// i sea you and you are ok