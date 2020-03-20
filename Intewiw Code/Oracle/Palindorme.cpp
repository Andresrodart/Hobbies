#include <stack>
#include <string>
using namespace std;
// apuntador a char, o string, evealuar si es un palindormo. ANacaNA

bool isPalindrome(string str){
    stack<char> stk;
    int len = str.size();
    if(len == 0) return true;
    char aux;
    for(int i = 0; i < len/2; i++)
        stk.push(str[i]);
    int pos = (len % 2 == 0)? len/2: ((len/2) + 1);
    for(int i = pos; i < len; i++){
        aux = stk.pop();
        if(aux != str[i]) return false;
    }
    return true;
}