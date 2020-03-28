#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

int main(int argc, char const *argv[]){
    unordered_map<char, int> aux = {
        {'a', 3},
        {'v', 5},
        {'b', 23},
        {'w', 33},
        {'z', 31},
    };
    for(auto var : aux)
        std::cout << var.second << std::endl;
    string str = "Hello World!";
    str.erase(remove_if(str.begin(), str.end(), ::isspace), str.end());
    std::cout << str << std::endl << (char) 300 << endl;
    return 0;
}