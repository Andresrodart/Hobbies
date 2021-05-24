#include <bits/stdc++.h>
#include <unordered_set>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

const intmax_t MAX_N = 1e5 + 1, MAX_K = 10;

vector<intmax_t> players;
uintmax_t tree[MAX_N] = {0};
std::vector<uintmax_t> ranking_of;

/**
 * @param childs_of a adjacency list of a tree, 0 must be root
*/
template<typename adjacencyL, typename NodeT>
std::stack<NodeT> post_order_iterative(adjacencyL childs_of);
/**
 * @param childs_of a adjacency list of a tree, 0 must be root
*/
template<typename adjacencyL, typename NodeT>
std::vector<uintmax_t> deep_of_nodes(adjacencyL childs_of, intmax_t number_of_nodes);

bool comparator (uintmax_t i,uintmax_t j) { return (ranking_of[i]>ranking_of[j]); }

int main(int argc, char const *argv[]){
    std::ios_base::sync_with_stdio(False);
    bool is_first;
    uintmax_t current_node;
    queue<uintmax_t> aux_queue;
    intmax_t aux, n, N, k, i = 1, next_player = 0;
    
    std::make_heap(players.begin(), players.end());
    
    cin >> n >> k;
    
    N = n;
    vector<vector<uintmax_t> > childs_of(N, vector<uintmax_t>());
    /*Insort en log(n) de los jugadores por poder
    * std::make_heap, std::pop_heap, std::push_heap, std::sort_heap
    */
    while (k--)
    {
		cin >> aux;
		players.push_back(aux);
        std::push_heap(players.begin(), players.end());
	}

    /*Construcción del árbol*/
    while (n-- > 1)
    {
		cin >> aux;
		childs_of[aux].push_back(i++);
	}

    /*Obtenemos el ranking de cada nodo*/
    /*O(2n)*/
    ranking_of = deep_of_nodes<vector<vector<uintmax_t> >, uintmax_t>(childs_of, N);
    
    /*Ordenamos las listas de adyacencia, para que el que tenga mas profundidad sea el primero que se procese*/
    //O(n lg n) 
    aux_queue.push(0);
    while (!aux_queue.empty()) // O(n lg n) 
    {
        current_node = aux_queue.front(); aux_queue.pop();
        for(uintmax_t child : childs_of[current_node])                                      // O(n)
            if(childs_of[child].size())
                aux_queue.push(child);
        sort(childs_of[current_node].begin(), childs_of[current_node].end(), comparator);   //O(n lg n)
    }
    
    /*Armamos el pleito*/
    // O(2n)
    tree[0] = players.front();
    std::pop_heap (players.begin(),players.end()); players.pop_back();
    aux_queue.push(0);
    while (!aux_queue.empty()) // O(n) 
    {
        is_first = true;
        current_node = aux_queue.front(); aux_queue.pop();
        for(uintmax_t child : childs_of[current_node])                                    // O(n)
        {
            if(is_first)
            {
                //Guardamos el jugador que le dimos al padre
                is_first = false;
                tree[child] = tree[current_node];
            }
            else
            {
                /*Si no es el mas profundo le damos el sigueinte peleador fuerte*/
                tree[child] = players.front();
                std::pop_heap (players.begin(),players.end()); players.pop_back();
            }
            aux_queue.push(child);
        }
    }
    
    /*Resultado*/
    // O(n) 
    uintmax_t res = 0;
    aux_queue.push(0);
    while (!aux_queue.empty()) // O(n) 
    {
        current_node = aux_queue.front(); aux_queue.pop();
        for(uintmax_t child : childs_of[current_node])
        {
            res += tree[child];
            aux_queue.push(child);
        }
    }
    std::cout << res;
    return 0;
}

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