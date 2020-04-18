#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

int main(int argc, char const *argv[]){
	int T, x, n, m;
	std::cin >> T;
	for (size_t i = 0; i < T; i++){
		std::cin >> x >> n >> m;
		while (x > 0);
			if ((x / 2) + 10 < x - 10 && n > 0) n--;
			else if(m > 0) m--;
			else break;
		if (x <= 0) std::cout << "YES" << std::endl;		
		else std::cout << "No" << std::endl;		
		
	}
	
	return 0;
}