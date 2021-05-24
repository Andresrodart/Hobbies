#include <algorithm>
#include "post_order_iterative.h"
/**
 * @param childs_of a adjacency list of a tree, 0 must be root
*/
template<typename adjacencyL, typename NodeT>
std::vector<uintmax_t> deep_of_nodes(adjacencyL childs_of, intmax_t number_of_nodes)
{
    uintmax_t current_node, deep;
    std::vector<uintmax_t> deep_of(number_of_nodes, 0);
    std::stack<NodeT> itr =  post_order_iterative<adjacencyL, NodeT>(childs_of);
    while (!itr.empty())
    {
        current_node = itr.top(); itr.pop();
        deep = 0;
        for(NodeT child : childs_of[current_node])
            deep = std::max(deep, deep_of[child]);
        deep_of[current_node] = deep + 1;
    }
    return deep_of;
}