#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

intmax_t LC(intmax_t IT, intmax_t LP,intmax_t CT){
    return (IT - CT) * LP;
}

intmax_t LR(intmax_t HP,intmax_t CT){
    return CT * HP;
}
intmax_t rate(intmax_t IT, intmax_t LP, intmax_t HP, intmax_t CT){
    return std::min(LC(IT, LP, CT), LR(HP, CT));
}



int main(int argc, char const *argv[]){
    std::ios_base::sync_with_stdio(False);
    intmax_t T = 0, IT, LP, HP, L, R, M, res = 0;
    std::cin >> T;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    while (T--){
        // std::cout << T <<  std::endl;
        std::cin >> IT >> LP >> HP;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
        L = 0, R = IT;
        for(int i = 0; i <= R; i++) std::cout << '\t' << rate(IT, LP, HP, i) << std::endl;
        while (L < R){
            M = (L + R) / 2;
            res = std::max(res, rate(IT, LP, HP, M));
            if(rate(IT, LP, HP, M) > rate(IT, LP, HP, M + 1)) R = M - 1;
            else L = M + 1;
        }
        std::cout << '>' << rate(IT, LP, HP, L) << std::endl;
        
    }
    return 0;
}