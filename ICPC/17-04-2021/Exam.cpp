#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

const intmax_t MAX_N = 1000, MAX_K = 10;

intmax_t n, k;
bool tests[MAX_N][10];
bool test_guide[10];
intmax_t mode_ans[10][2];

class BoolNum{
    private:
        std::vector<bool> number = {};
        intmax_t next = -1;
    public:
        BoolNum(intmax_t size);
        std::vector<bool> getNext();
};

BoolNum::BoolNum(intmax_t size){
    for (size_t i = 0; i < size; i++)
        number.push_back(False);
}

std::vector<bool> BoolNum::getNext(){
    if(next++ == 0) return number;
    bool carry = True;
    for (size_t i = 0; i < number.size(); i++){
        if(carry){
            if(number[i]) number[i] = False, carry = True;
            else number[i] = True, carry = False;
        }
    }
    return number;
}


intmax_t calc_min_cal(std::vector<bool> answers){
    intmax_t min_cal = INT_MAX;
    for (size_t i = 0; i < n; i++){
        intmax_t cur_cal = 0;
        for (size_t j = 0; j < k; j++){
            //std::cout << "\t" << i << " - " << j << " -> " << tests[i][j] << " vs " << test_guide[j] << std::endl;
            cur_cal += (tests[i][j] == answers[j])? 1:0;
        }
        //std::cout << cur_cal << std::endl;
        min_cal = min(min_cal, cur_cal);
    }
    return min_cal;
}

int main(int argc, char const *argv[]){
    std::ios_base::sync_with_stdio(False);
    intmax_t min_cal = -1;
    std::string test;
    std::cin >> n >> k;
    BoolNum combinations(k);
    std::vector<bool> last(k);
    
    for (size_t i = 0; i < n; i++){
        std::cin >> test;
        for (size_t j = 0; j < k; j++){
            tests[i][j] = test[j] == 'T';
            last[j] = True;
        }
    }
    std::vector<bool> number;
    do{
        number = combinations.getNext();
        min_cal = max(min_cal, calc_min_cal(number));
        // for(auto var : number)
        //      std::cout << var << " ";
        // std::cout << std::endl;
    } while (number != last);
    
    std::cout << min_cal << std::endl;
    
    return 0;
}