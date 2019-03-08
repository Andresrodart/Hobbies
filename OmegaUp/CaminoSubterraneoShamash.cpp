#include <iostream>

void babiNum(int input){
    if (input >= 60) {
        int unit = input/60;
        babiNum(input - unit*60);
        std::cout << ".";
        babiNum(unit);
    }
    else{
        while(input >= 10){
        std::cout << "L";
        input = input - 10;
        }
        while(input > 0){
            std::cout << "I";
            input = input - 1;
        }
    }
}

int main(int argc, char const *argv[]){
    int input, auxState;
    std::cin >> input;
    babiNum(input);
        
    return 0;
}
