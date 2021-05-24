#include <bits/stdc++.h>
#include <unordered_set>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
#include "deep_of_nodes.h"
using namespace std;

/*Definir el tree - Deepnest
        0           3
       / \
      1   2      2     1   
     / \   
    3   4      1   1 
*/
vector<vector<uintmax_t> > adjacency_list
{
    {1, 2}, // 0
    {3, 4},  // 1
    {},     // 2
    {},     // 3
    {},     // 4
};

int main(int argc, char const *argv[]){
    std::ios_base::sync_with_stdio(False);
    vector<uintmax_t> deep_of = deep_of_nodes<std::vector<std::vector<uintmax_t> >, uintmax_t>(adjacency_list, 5);
    for(auto deep : deep_of)
        std::cout << deep << " ";
    std::cout << std::endl;
    return 0;
}