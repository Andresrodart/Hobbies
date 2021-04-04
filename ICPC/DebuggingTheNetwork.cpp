#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

const intmax_t MAXN = 10e6;
std::string str; 

bool isfeasible(intmax_t k){
    intmax_t len = 0, i = 0;
    while (i < str.size()){
        intmax_t times = 0, decimal = 0;
        while (isdigit(str[i])){
            if(decimal > 0) times *= 10;
            times += str[i++] - '0';
            decimal++;
        }
        if (times == 0) len++;
        else len += times;
        i++;
    }
    return len <= k;
}

int main(int argc, char const *argv[]){
    intmax_t T, k;
    std::ios_base::sync_with_stdio(False);
    std::cin >> T;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
    while (T--){
        intmax_t i = 0, j = 1, pos = 0;
        std::string res;
        std::cin >> str >> k;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
        if(str.size() == 1){
            std::cout << str << std::endl;
            continue;
        }
        else if(isfeasible(k)){
            while (i < str.size()){
                intmax_t times = 0, decimal = 0;
                while (isdigit(str[i])){
                    if(decimal > 0) times *= 10;
                    times += str[i++] - '0';
                    decimal ++;
                }
                for(intmax_t x = 0; x < times; x++) std::cout << str[i];
                if (times == 0) std::cout << str[i];
                i++;
            }
            std::cout << std::endl;
        }else std::cout << "unfeasible" << std::endl;
    }
    return 0;
}