#include <stack>
#include <vector>
/**
 * @param childs_of a adjacency list of a tree, 0 must be root
*/
template<typename adjacencyL, typename NodeT>
std::stack<NodeT> post_order_iterative(adjacencyL childs_of)
{
    NodeT current_node;
    std::stack<NodeT> aux_stack, post_order_stack;
    /*Assuming 0 is the root*/
    aux_stack.push(0);
    while (!aux_stack.empty())
    {
        current_node = aux_stack.top(); aux_stack.pop();
        for(NodeT child : childs_of[current_node])
            aux_stack.push(child);
        post_order_stack.push(current_node);
    }
    return post_order_stack;
}