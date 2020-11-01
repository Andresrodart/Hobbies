#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

std::string dfs(std::string u, std::unordered_map< std::string, std::vector<std::string> > &nodes){
	std::unordered_set<std::string> visited;
	std::stack<std::string> stack; stack.push(u);
	std::string min_item = u;
	while (stack.size() > 0){
		u = stack.top(); stack.pop();
		std::unordered_set<std::string>::const_iterator got = visited.find(u);
		if (got == visited.end()){
			// std::cout << "min_item " << u <<std::endl; 
			visited.insert(u);
			if (min_item.size() == u.size()) 
				min_item = (std::lexicographical_compare(min_item.begin(), min_item.end(), u.begin(), u.end()))? min_item: u;
			else
				min_item = (min_item.size() < u.size())? min_item: u;
			for (auto child: nodes[u]) stack.push(child);
		}
	}
	return min_item;
}
int main(int argc, char const *argv[]){
	std::ios_base::sync_with_stdio(False);
	uintmax_t N;
	std::string u, v;
	std::cin >> N;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	std::unordered_map< std::string, std::vector<std::string> > nodes;
	while (N--){
		std::cin >> u >> v;
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		nodes[u].push_back(v); //.insert(std::make_pair(u, std::vector<std::string> ()));
		nodes[v].push_back(u);
	}

	std::string message;
	std::getline(std::cin, message);
	std::istringstream ss(message);
    std::string word; // for storing each word

    while (ss >> word){
		// std::unordered_map< std::string, std::vector<std::string> >::const_iterator got = nodes.find (word);
		if (nodes[word].size() > 0) std::cout << dfs(word, nodes) << " ";
		else std::cout << word << " ";
    }
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