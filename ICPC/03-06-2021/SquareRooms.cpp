#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

char input[100][100], output[100][100], room = 'A';
bool used[100][100];
int64_t row, column;

int just_one(int64_t sqr_size, int64_t first, int64_t second){
	int64_t count = 0;
	//cout << "\t square size" << sqr_size << endl;
	for (size_t ii = 0; ii < sqr_size; ii++){
		for (size_t jj = 0; jj < sqr_size; jj++){
			if(input[ii + first][jj + second] == '#' || output[ii + first][jj + second] != '-') count = 2;//return false;
			else if(input[ii + first][jj + second] == '$') count++;
			//cout << '\t' << input[ii + first][jj + second];
		}
		//cout << endl;
	}
	//cout << '\t' << count << endl;
	return (count == 1)? 0:((count > 1)? 1:-1);
}

void print_grid(){
	for (size_t i = 0; i < row; i++){
		for (size_t j = 0; j < column; j++){
			cout << output[i][j];
		}
		cout << endl;
	}
}
void print_grid(int a){
	for (size_t i = 0; i < row; i++){
		for (size_t j = 0; j < column; j++){
			cout << '\t' << input[i][j];
		}
		cout << endl;
	}
}
pair<intmax_t, intmax_t> next_cell(){
	for (size_t i = 0; i < row; i++){
		for (size_t j = 0; j < column; j++){
			if(!used[i][j]) return make_pair(i, j);
		}
	}
	return make_pair(-1, -1);
}

bool find_rooms(pair< intmax_t, intmax_t > ij){
	if(ij.first == -1) return true;
	intmax_t max_sqr_size = min(row - ij.first, column - ij.second);
	while (true){
		//cout << "max_sqr " <<  max_sqr_size << " ij " << ij.first << '-' << ij.second << endl;
		/*busqueda binaria para encontrar el cuadro mas grande con un solo tesoro*/
		/*right es el cuadro mas grande que podemos aceptar, debe estar basado en el backtracking*/
		int64_t left = 1, right = max_sqr_size, mid, max_square = 0;
		while (left <= right){																	//O(log(100^2))
			mid = (left + right) / 2;
			intmax_t bb = just_one(mid, ij.first, ij.second);
			if(bb == 0) max_square = mid, left = mid + 1; 	//O(100^2)
			else if (bb > 0) right = mid - 1;
			else left = mid + 1;
		}
		if(max_square){
			for (size_t i = 0; i < max_square; i++){
				for (size_t j = 0; j < max_square; j++){
					output[i + ij.first][j + ij.second] = room;
					used[i + ij.first][j + ij.second] = true;
				}
			}
			/*Si regresamos, no podemos usar el mismo cuadrado grande, debemos tratar con cuadrados menores*/
			max_sqr_size = max_square - 1;
			room++;
		}
		else{
			room--;
			return false;
		}
		//print_grid();
		if(find_rooms(next_cell())) break;
		for (size_t i = 0; i < max_square; i++){
			for (size_t j = 0; j < max_square; j++){
				used[i + ij.first][j + ij.second] = false;
				output[i + ij.first][j + ij.second] = '-';
			}
		}
	}
	return true;
}

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(False);
	char cell;
	bool failed = false;
	vector< pair<intmax_t, intmax_t>> steps;
	map< pair<intmax_t, intmax_t>, intmax_t > sizes; 
	cin >> row >> column;
	for (size_t i = 0; i < row; i++){
		for (size_t j = 0; j < column; j++){
			cin >> input[i][j];
			//if(input[i][j] == '#') output[i][j] = '#';
			output[i][j] = (input[i][j] == '#')? '#':'-';
			used[i][j] = (input[i][j] == '#')? true:false;
		}
	}
	//print_grid(1);
	if(!find_rooms(make_pair(0, 0))) cout << "elgnatcer\n";
	else{print_grid();}
	return 0;
}