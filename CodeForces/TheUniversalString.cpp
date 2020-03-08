#include <iostream>
#include <string>
#define ll long long
using namespace std;

int main(int argc, char const *argv[]){
    ll T;
    string query;
    cin >> T;
    while (T--){
        string res = "YES";
        cin >> query;
        for (size_t i = 1; i < query.size(); i++)
            if(query[i - 1] != query[i] - 1 && query[i - 1] != 'z' && query[i] != 'a')
                res = "NO";
        cout << res << "\n";
    }
    return 0;
}