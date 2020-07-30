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

vector<vector<uint32_t> > zeroMatrix(vector<vector<uint32_t> > matrix){
	for (size_t i = 0; i < matrix.size(); i++){
		for (size_t j = 0; j < matrix[0].size(); j++){
			if (matrix[i][j] == 0){
				for (size_t k = 0; k < matrix.size(); k++) matrix[k][j] = NULL;
				for (size_t k = 0; k < matrix[0].size(); k++) matrix[i][k] = NULL;
			}
		}
	}
	for (size_t i = 0; i < matrix.size(); i++)
		for (size_t j = 0; j < matrix[0].size(); j++)
			if(matrix[i][j] == NULL) matrix[i][j] = 0;
	return matrix;
}

int main(int argc, char const **argv){
	print_matrix(zeroMatrix({
		{1, 0, 3, 4, 5},
		{16, 17, 18, 0, 6},
		{15, 24, 25, 20, 7},
		{14, 0, 22, 21, 8},
		{0, 12, 11, 10, 9},
	}));
	return 0;
}