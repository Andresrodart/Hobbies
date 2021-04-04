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
std::map<std::pair<intmax_t,intmax_t>, intmax_t> mp;
std::map<std::pair<intmax_t,intmax_t>, intmax_t> banned;

void dijkstra(intmax_t start){
	intmax_t u;
	for( intmax_t i = 1; i < n; i++) distances[i] = INTMAX_MAX; 
	heap.push(start);
	
	while(heap.size()){
		u = heap.top(); heap.pop();
		for(intmax_t i = 0; i < adjacent[u].size(); i++){
			intmax_t v = adjacent[u][i];
			intmax_t weight = mp[{u, v}]; 
			if(distances[u] + weight < distances[v] && weight != INTMAX_MAX) 
				distances[v] = distances[u] + weight, prev[v] = u, heap.push(v);
		}
	}
}

void reverseIteration(intmax_t pos, std::deque<intmax_t> &triplet){
	triplet.push_front(pos);
	if(triplet.size() > 3) triplet.pop_back();
	if (pos != 0 && pos != INTMAX_MAX) reverseIteration(prev[pos], triplet);
	std::cout << pos + 1 << ' ';
	if(banned[{triplet[0], triplet[1]}] == triplet[2]) std::cout << triplet[1] << ' ' << triplet[2] << ' ';
}

int main(int argc, char const *argv[]){
	intmax_t m, u, v, k, a, b, c, weitgh = 1, aux[3];
	std::deque<intmax_t > triplet;
	std::ios_base::sync_with_stdio(False);
	std::cin >> n >> m >> k;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	while(m--){
		std::cin >> u >> v;
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		adjacent[u - 1].push_back(v - 1);
		adjacent[v - 1].push_back(u - 1);
		mp[{u - 1, v - 1}] = weitgh;
		mp[{v - 1, u - 1}] = weitgh;
	}
    while (k--){
		std::cin >> aux[0] >> aux[1] >> aux[2];
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		banned[{aux[0], aux[1]}] = aux[2];
    }
	dijkstra(0);
	if (distances[n - 1] == INTMAX_MAX) std::cout << -1 << std::endl;
	else std::cout << distances[n - 1] << std::endl, reverseIteration(n - 1, triplet);
	return 0;
}
