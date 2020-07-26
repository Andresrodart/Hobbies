#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

void print_matrix(vector<vector<uint32_t> > matrix){
	cout << "----------------" << endl;
	for(auto line: matrix) {
		for (auto num: line) cout << num << '\t' ;
		std::cout << std::endl;
	}
}

vector<vector<uint32_t> > rotateMatrix(vector<vector<uint32_t> > matrix){
	uint32_t N = matrix[0].size();
	for (size_t j = 0; j < N / 2; j++){		// O(n^2)
		for (size_t i = 0; i < N - 1 - 2 * j; i++){ // O(n)
			swap(matrix[j][i + j], matrix[i + j][N - 1 - j]); 	// O(1)
			swap(matrix[j][i + j], matrix[N - 1 - j][N - i - 1 - j]);	// O(1)
			swap(matrix[j][i + j], matrix[N - i - 1 - j][j]);			// O(1)
		}	
	}
	return matrix;
}

int main(int argc, char const **argv){
	print_matrix(rotateMatrix({
		{1, 2, 3, 4, 5},
		{16, 17, 18, 19, 6},
		{15, 24, 25, 20, 7},
		{14, 23, 22, 21, 8},
		{13, 12, 11, 10, 9},
	}));
	return 0;
}
