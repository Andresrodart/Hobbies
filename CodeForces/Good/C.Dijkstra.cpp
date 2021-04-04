#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

#define MAXN 1000000

intmax_t n = MAXN;
std::vector< intmax_t> adjacent[MAXN];
std::priority_queue<intmax_t> heap;
intmax_t distances[MAXN] {0};
intmax_t prev[MAXN] = {INTMAX_MAX};
std::map<std::pair<intmax_t,intmax_t>,intmax_t>mp;

void dijkstra(intmax_t start){
	intmax_t u;
	for( intmax_t i = 1; i < n; i++) distances[i] = INTMAX_MAX; 
	heap.push(start);
	
	while(heap.size()){
		u = heap.top(); heap.pop();
		for(intmax_t i = 0; i < adjacent[u].size(); i++){
			intmax_t v = adjacent[u][i];
			intmax_t weight = mp[{u, v}]; 
			if(distances[u] + weight < distances[v]) 
				distances[v] = distances[u] + weight, prev[v] = u, heap.push(v);
		}
	}
}

void reverseIteration(intmax_t pos){
	if (pos != 0 && pos != INTMAX_MAX) reverseIteration(prev[pos]);
	std::cout << pos + 1 << ' ';
}

int main(int argc, char const *argv[]){
	intmax_t m, u, v, weitgh;
	std::ios_base::sync_with_stdio(False);
	std::cin >> n >> m;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	while(m--){
		std::cin >> u >> v >> weitgh;
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		adjacent[u - 1].push_back(v - 1);
		adjacent[v - 1].push_back(u - 1);
		mp[{u - 1, v - 1}] = weitgh;
		mp[{v - 1, u - 1}] = weitgh;
	}
	dijkstra(0);
	if (distances[n - 1] == INTMAX_MAX) std::cout << -1 << std::endl;
	else reverseIteration(n - 1);
	return 0;
}