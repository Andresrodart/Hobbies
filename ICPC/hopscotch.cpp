#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

class edge{
	public:
	intmax_t distance;
	std::pair<intmax_t, intmax_t> cord;
	edge(intmax_t distance, std::pair<intmax_t, intmax_t> cord){
		this -> distance = distance;
		this -> cord = cord;
	}
	bool operator<(edge other) const{
        return this -> distance > other.distance;
    }
};

const intmax_t n = 50;
const intmax_t n__2 = 2500;
intmax_t grid[n][n];
bool visited[n][n];
std::vector< std::vector<edge > > points {n__2, std::vector<edge>() };

intmax_t dijkstra(intmax_t k){
	std::priority_queue<edge> heap;
	for(intmax_t point = 0; point < points[0].size(); point++){
		points[0][point].distance = 0;
		heap.push(points[0][point]);
	}
	
	while(heap.size() > 0){
		edge v = heap.top(); heap.pop();
		intmax_t i = v.cord.first, j = v.cord.second;
		if(grid[i][j] == k)	return v.distance;
		if(!visited[i][j]){
			visited[i][j] = True;
			for(intmax_t point = 0; point < points[grid[i][j]].size(); point++){
					edge u = points[grid[i][j]][point];
					intmax_t nx = u.cord.first, ny = u.cord.second;
					points[grid[i][j]][point].distance = std::min( std::abs(i - nx) + std::abs(j - ny) + v.distance, u.distance);
					heap.push(points[grid[i][j]][point]);
			}
		}
			
	}
	return INTMAX_MAX;
}
			

int main(int argc, char const *argv[]){
	std::ios_base::sync_with_stdio(False);
	intmax_t n_, k, res = INTMAX_MAX;
	std::cin >> n_ >> k;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for(intmax_t i = 0; i < n_; i ++){
		for(intmax_t j = 0; j < n_; j ++){
			std::cin >> grid[i][j];
			points[grid[i][j] - 1].push_back(edge(INTMAX_MAX, std::make_pair(i, j)));
			visited[i][j] = False;
		}
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	}
	res = dijkstra(k);
	std::cout << ((res == INTMAX_MAX)? -1 : res) << std::endl;
	return 0;
}

