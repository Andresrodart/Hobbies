#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

intmax_t max_n = 10e5;
intmax_t b = 1;
intmax_t c = std::tgamma(b + 1);
intmax_t facs[(int) 10e5];
void init_facs(){
	facs[b] = c;
	while (c < max_n){
		c = std::tgamma(b + 1);
		facs[b] = c;
		b ++;
	}
}

intmax_t recu(intmax_t N, intmax_t i, intmax_t sum){
	std::cout << sum << std::endl;
	if (sum + facs[i] == N) return i;
	else if(i >= 10 || facs[i] > N) return 10e5;
	return std::min(recu(N, i + 1, sum), recu(N, i + 1, sum + facs[i]));
}

intmax_t solve(intmax_t N){
	return recu(N, 1, 0);
}


int main(int argc, char const *argv[]){
	init_facs();
	std::ios_base::sync_with_stdio(False);
	intmax_t N;
	b = 1;
	
	while (facs[b] < max_n){
		std::cout << facs[b] << " - " << b << std::endl;
		b ++;
	}
	std:: cin >> N;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	std::cout << solve(N) << std::endl;
	return 0;
}