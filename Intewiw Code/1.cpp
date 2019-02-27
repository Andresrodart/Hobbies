#include <iostream>
#include <string>
int main()
{
    std::string n_and_t;
    std::string line;
    
    std::getline(std::cin, n_and_t );
    std::cin >> line;

    std::string::size_type sz;   // alias of size_t
    
    int pos = n_and_t.find(' ');
    int n = std::stoi(n_and_t.substr(0, pos), &sz) - 1;
    int t = std::stoi(n_and_t.substr(pos), &sz);
    for (int j = 0; j < t; j++)
    {
        for(int i = 0;i < n ; i++)
        {
            char next = line.at( i + 1 );
            if (next == 'G' && line.at( i ) == 'B')
            {
                line.at( i + 1 ) = 'B';
                line.at( i ) = 'G';
                i++;
            }   
        }
    }

    std::cout << line << '\n';
    return 0;
}