#include <bits/stdc++.h>
using namespace std;

unordered_set<string> dp = {};
unordered_set<string> indexes = {};

void generateSubsString(string text, string unused, int64_t begin, int64_t end){
    if(end == text.size()) return;
    unused += text[end];
    string textRange = to_string(begin) + "-" + to_string(end);
    if(indexes.find(textRange) != indexes.end()) return;
    dp.insert(unused);
    indexes.insert(textRange);
    generateSubsString(text, unused, begin, end + 1);
    generateSubsString(text, "", end + 1, end + 1);
}
long long int subStrings(string text){
    dp = {};
    indexes = {};
    generateSubsString(text, "", 0, 0);
    return dp.size();
}

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);
    string s;
    long long int W, Q, index, res;
    while(cin >> s){
        cin >> Q >> W;
        while(Q--){
            cin >> index;
            res = subStrings(s.substr(index - 1, W));
            cout << res << '\n';
        }
    }
    return 0;
}
