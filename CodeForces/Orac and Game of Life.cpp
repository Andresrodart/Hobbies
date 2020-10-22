#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
const int MAXN = 1005;
int res[MAXN][MAXN];
std::pair<int, int> _queue[MAXN * MAXN];
std::vector<bool> aux(MAXN, false);
std::vector< std::vector<bool>>visited(MAXN, aux);
int pos[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

int matrix[MAXN][MAXN];
int min(int a, int b, int c, int d){
	int res = a;
	res = (res < b)? res:b; 
	res = (res < c)? res:c; 
	res = (res < d)? res:d; 
	return res;
}
void bfs(/*std::vector< std::string> &matrix*/int n, int m){
	// std::queue< std::pair<int, int>> _queue;
	std::pair <int,int> _pair;
	long long int front = 0, back = 0;
	for (size_t i = 0; i < n; i++)
		for (size_t j = 0; j < m; j++){
			int node = matrix[i][j];
			res[i][j] = 1005;
			if ((i > 0 && matrix[i - 1][j] == node) || (j > 0 && matrix[i][j - 1] == node) || (i + 1 < n && matrix[i + 1][j] == node) || (j + 1 < m && matrix[i][j + 1] == node)){
				res[i][j] = 0;
				if ((i > 0 && matrix[i - 1][j] != node) || (j > 0 && matrix[i][j - 1] != node) || (i + 1 < n && matrix[i + 1][j] != node) || (j + 1 < m && matrix[i][j + 1] != node))
					_queue[back++] = std::make_pair(i, j);//.push(std::make_pair(i, j));
				visited[i][j] = True;
			}
		}
	while (/*_queue.size() > 0*/ front < back){
		_pair = _queue[front++];//.front();
		//_queue.pop();
		int i = _pair.first;
		int j = _pair.second;
		int up = 1005, down = 1005, left = 1005, right = 1005;
		for(int x = 0; x < 4; x++){
			int nx = i + pos[x][0], ny = j + pos[x][1];
			if(nx < 0 || nx > n || ny < 0 || ny > m || visited[nx][ny])
				continue;
			res[nx][ny] = res[i][j] + 1;
			visited[nx][ny] = True;
			_queue[back++] = std::make_pair(nx,ny);
		}
		// if (i > 0){
		// 	if (!visited[i - 1][j]) _queue[back++] = std::make_pair(i - 1, j);//.push(std::make_pair(i - 1, j));
		// 	up = res[i - 1][j];
		// }
		// if (j > 0){
		// 	if (!visited[i][j - 1]) _queue[back++] = std::make_pair(i, j - 1);//.push(std::make_pair(i, j - 1));
		// 	left = res[i][j - 1];
		// }
		// if(i + 1 < n){
		// 	if (!visited[i + 1][j]) _queue[back++] = std::make_pair(i + 1, j);//_queue.push(std::make_pair(i + 1, j));
		// 	down = res[i + 1][j];
		// }
		// if (j + 1 < m){
		// 	if (!visited[i][j + 1]) _queue[back++] = std::make_pair(i, j + 1);//_queue.push(std::make_pair(i, j + 1));
		// 	right = res[i][j + 1];
		// }
		// if (!visited[i][j]){
		// 	res[i][j] = min(up, down, left, right) + 1;
		// 	visited[i][j] = True;
		// }
	}
}

int main(int argc, char const *argv[]){
	int n, m, i, j;
	long long int t, p, when;
	std::ios_base::sync_with_stdio(False);
	std::cin >> n >> m >> t; 
	// std::vector<std::string> matrix;
	std::string str;
	getline(std::cin, str);
	for (i = 0; i < n; i++){
		getline(std::cin, str);
		for(j = 0;	j < m; j++) 
			matrix[i][j] = str[j] - '0';
	}
	
	bfs(/*matrix*/n, m);
	// for ( i = 0; i < n; i++){
	// 	for (j = 0; j < m; j++){
	// 		std::cout << res[i][j] << " " ;
	// 	}
	// 	std::cout << std::endl;
	// }
	
	while (t > 0) {
		std::cin >> i >> j >> p;
		if (!visited[i - 1][j - 1]) std::cout << matrix[i - 1][j - 1] << std::endl;
		else{
			when = res[i - 1][j - 1];
			if ((p + when) % 2 == 0 || when >= p) std::cout << matrix[i - 1][j - 1] << std::endl;
			else std::cout << ((matrix[i - 1][j - 1] == 1)? 0:1) << std::endl;
		}
		t -= 1;
	}
	return 0;
}
// 3 2 1 0 0
// 2 1 0 0 1
// 1 0 0 1 2
// 0 0 1 2 3
// 0 1 2 3 4