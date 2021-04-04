#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
const intmax_t MAXN = 10e6 + 1;
std::vector<intmax_t> result(MAXN, INTMAX_MAX);
std::vector<intmax_t> levels[MAXN];
std::set<intmax_t> iterators;
intmax_t performance[MAXN];
intmax_t N, B, min_ = INTMAX_MAX, max_ = 0;

int main(int argc, char const *argv[]){
    intmax_t multiplaier = 1;
    std::ios_base::sync_with_stdio(False);
    std::cin >> N >> B;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for (intmax_t i = 0; i < N; i++){
        std::cin >> performance[i];
        levels[performance[i]].push_back(i);
        iterators.insert(performance[i]);
    }
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        
    for (intmax_t i : iterators){
        if(i == 0) for(intmax_t index = 0; index < levels[i].size(); index++) result[levels[i][index]] = 0;
        else for(intmax_t j = 0; j < levels[i].size(); j++){
            intmax_t index = levels[i][j];
            intmax_t prev = (index == 0)? result[N - 1]:result[index - 1];
            intmax_t next = (index == N - 1)? result[0]:result[index + 1];
            intmax_t p_prev = (index == 0)? performance[N - 1]:performance[index - 1];
            intmax_t p_next = (index == N - 1)? performance[0]:performance[index + 1];
            if(prev == INTMAX_MAX && next == INTMAX_MAX) result[index] = B;
            else if((p_prev == performance[index] && p_next == performance[index]) && std::min(prev, next) != INTMAX_MAX) result[index] = std::min(prev, next);
            else if(p_prev == performance[index] && p_prev != INTMAX_MAX) result[index] = prev;
            else if(p_next == performance[index] && p_next != INTMAX_MAX) result[index] = next;
            else if(prev == INTMAX_MAX) result[index] = ((next / B) + 1) * B;
            else if(next == INTMAX_MAX) result[index] = ((prev / B) + 1) * B;
            else result[index] = ((std::max(prev, next) / B) + 1) * B;
        }
    }
    for (intmax_t i = 0; i < N - 1; i++)
        std::cout << result[i] << ' '; 
    std::cout<< result[N - 1] <<std::endl;    
    
    return 0;
}