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

int main(int argc, char const *argv[]){
	intmax_t u, v, weitgh;
	// for(size_t i = 0; i < MAXN; i++) distances.push_back( node(i));
	std::ios_base::sync_with_stdio(False);
	for(int i = 0; i < 14; i++){
		std::cin >> u >> v >> weitgh;
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
		adjacent[u].push_back(v);
		adjacent[v].push_back(u);
		mp[{u,v}] = weitgh;
		mp[{v,u}] = weitgh;
	}
	dijkstra(0);
	for(int i = 0; i < 9; i++)
		std::cout << "distance to: " << i << " is: " << distances[i] << " comes from: " << prev[i] << std::endl;
	return 0;
}

/*
Drive: 

0 1 4
0 7 8
1 2 8
1 7 11
7 8 7
7 6 1
2 3 7
2 5 4
2 8 2
8 6 6
6 5 2
3 4 9
3 5 14
5 4 10

Expected Output
Vertex   Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14


bool visited[MAXN] = {False};
bool cmp(intmax_t a, intmax_t b){
	return distances[a] > distances[b];
}

intmax_t dijkstra(intmax_t start){
	std::deque<intmax_t> heap;
	distances[start] = 0;
	heap.push_back(start);
	std::make_heap(heap.begin(), heap.end(), cmp);
	while (heap.size() > 0){
		intmax_t v = heap.front(); heap.pop_front();
		if(!visited[v]){
			// std::cout << "processing: " << v << std::endl;
			visited[v] = True;
			for(intmax_t goTo = 0; goTo < adjacent[v].size(); goTo++){
				intmax_t u = adjacent[v][goTo].first;
				// std::cout << "\tfrom: " << v << " to: "<< u << " costs: " << distances[u] << " min disnance is min between: " << distances[v] << " + " << adjacent[v][goTo].second << " and " << distances[u] << std::endl;
				if(distances[v] + adjacent[v][goTo].second < distances[u]){
					distances[u] = distances[v] + adjacent[v][goTo].second;
					prev[u] = v;
				}
				heap.push_back(u);
				std::make_heap(heap.begin(), heap.end(), cmp);
			}
		}
	}
}

class node{
	public:
		bool visited = False;
		intmax_t id = INTMAX_MAX;
		intmax_t prev = INTMAX_MAX;
		intmax_t distance = INTMAX_MAX;
		std::vector< std::pair<intmax_t, intmax_t>>  destinies;
		node(intmax_t id){
			this -> id = id;
		}
		void addDestiny(intmax_t v, intmax_t weight){
			this -> destinies.push_back(std::make_pair(v, weight));
		}
		bool operator<(node other) const{
			return this -> distance > other.distance;
		}
};

std::vector<node> distances;

*/