#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
char grid[40][40];
int collitions[40][40] = {};
int L, C, N;
std::string aux;
std::vector<std::string > words_(20); 
std::vector<std::unordered_map<char, long long int> > words(20); 

int checkCol(int i, int j, std::unordered_map<char, long long int> x, int val){
    for(int k = 0; k < x.size(); k++){
        if(i >= L || j >= C) return 0;
        if(x.find(grid[i][j]) == x.end() || x[grid[i][j]] == 0) return 0;
        x[grid[i][j]] -= 1;
        i++;
    }
    for(int k = 0; k < x.size() && i >= 0; k++){
        i--;
        if(collitions[i][j] == 0) collitions[i][j] = val;
        else if(collitions[i][j] != 0 && collitions[i][j] != val) collitions[i][j] = -1;
    }
    return 1;
}
int checkDig(int i, int j, std::unordered_map<char, long long int> x, int val){
    for(int k = 0; k < x.size(); k++){
        if(i >= L || j >= C) return 0;
        if(x.find(grid[i][j]) == x.end() || x[grid[i][j]] == 0) return 0;
        x[grid[i][j]] -= 1;
        i++;
        j++;
    }
    for(int k = 0; k < x.size() && i >= 0 && j >= 0; k++){
        i--;
        j--;
        if(collitions[i][j] == 0) collitions[i][j] = val;
        else if(collitions[i][j] != 0 && collitions[i][j] != val) collitions[i][j] = -1;
    }
     return 0;
}
int checkRow(int i, int j, std::unordered_map<char, long long int> x, int val){
    for(int k = 0; k < x.size(); k++){
        if(i >= L || j >= C) return 0;
        if(x.find(grid[i][j]) == x.end() || x[grid[i][j]] == 0) return 0;
        x[grid[i][j]] -= 1;
        j++;
    }
    for(int k = 0; k < x.size() && j >= 0; k++){
        j--;
        if(collitions[i][j] == 0) collitions[i][j] = val;
        else if(collitions[i][j] != 0 && collitions[i][j] != val) collitions[i][j] = -1;
    }
     return 0;
}

int main(){
    int res = 0;
    std::ios_base::sync_with_stdio(False);
    std::cin >> L >> C;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for(int i = 0; i < L; i ++){
        for(int j = 0; j < C; j ++){
            collitions[i][j] = 0;
            std::cin >> grid[i][j]; 
        }
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');     
    }

    std::cin >> N;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for(int i = 0; i < N; i ++){
        std::cin >> aux;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        words_[i] = aux;
        for(auto letter: aux){
            if(words[i].find(letter) == words[i].end()) words[i][letter] = 1;
            else words[i][letter] += 1;
        }
    }
    for(int x = 0; x < N; x ++){
        for(int i = 0; i < L; i ++){
            for(int j = 0; j < C; j ++){
                checkRow(i, j, words[x], x + 1);
                checkCol(i, j, words[x], x + 1);
                checkDig(i, j, words[x], x + 1);
            }
        }
    }
    for(int i = 0; i < L; i ++){
        for(int j = 0; j < C; j ++){
            if(collitions[i][j] == -1) res ++;
        }
    }
    std::cout << res;
    return 0;
}
