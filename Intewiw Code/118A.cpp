#include <iostream>
#include <algorithm>


int main(void){
    vector<char> v = {'h', 'o', 'l', 'a'};
    string in;
    cin >> in;
    
    for (int i = 0; i < in.size(); i++) {

    }
    std::string ans = "";
    std::string in = "";
    std::getline(std::cin, in);
    std::transform(in.begin(), in.end(), in.begin(), ::tolower);

    for(int i = 0;i < in.size(); i++){
         if(in[i] != 'a' && in[i] != 'e' && in[i] != 'i' && in[i] != 'o' && in[i] != 'u' && in[i] != 'y'){
             ans.push_back('.');
             ans.push_back(in.at(i));
         } 
    }
    std::cout << ans;

    return 0;
}