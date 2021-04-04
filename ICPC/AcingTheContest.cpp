#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

std::unordered_map<intmax_t,intmax_t> DP;
std::vector<intmax_t> E(100);
std::vector<intmax_t> D(100);
std::vector<intmax_t> S(100);
intmax_t T, P;
intmax_t res;

int solv(std::vector<intmax_t> E, std::vector<intmax_t> D, std::vector<intmax_t> S, int member, int problem, int res){
    if(problem >= P || member >= T) return res;
    if(problem < P && ++member)  problem = 0;
    if(D[member] <= E[problem]){
        intmax_t prev = solv(E, D, S, member, problem + 1);
        E[member] -= E[problem];
        intmax_t next = solv(E, D, S, member, problem + 1) + S[problem];
        res += std::max(prev, next);
    }else
        res += solv(E, D, S, member, problem + 1);

    return res;
}
int main(int argc, char const *argv[]){
    std::ios_base::sync_with_stdio(False);
    std::cin >> T >> P;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for (size_t i = 0; i < T; i++)
        std::cin >> E[i];
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for (size_t i = 0; i < P; i++)
        std::cin >> D[i];
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    for (size_t i = 0; i < P; i++)
        std::cin >> S[i];    
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 

    res = 0;
    
    return 0;
}