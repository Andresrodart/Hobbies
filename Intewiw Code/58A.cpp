#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
    vector<char> v = {'h', 'e', 'l', 'l', 'o'};
    string in;
    cin >> in;
    int c = 0;
    for (int i = 0; i < in.size(); i++) {
        if (in[i] == v[c])
            c++;
    }
    if (c == 5)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}