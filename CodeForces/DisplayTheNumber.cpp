#include <iostream>

int main(int argc, const char** argv) {
	int segments, time;
	std::cin >> time;
	for (int i = 0; i < time; i++){
		std::cin >> segments;
		if(segments % 2 != 0){
			std::cout << 7;
			segments -= 3;
		}
		while (segments > 0){
			std::cout << 1;
			segments -= 2;
		}
		std::cout << std::endl;
	}
	
	return 0;
}