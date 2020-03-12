#include <stdio.h>
#define ll long long 
int main(int argc, char const *argv[]){
	ll cases, wins, palaces, row, col;
	scanf("%lld", &cases);
	for(int i = 0; i < cases; i++){
		wins = 0;
		scanf("%lld", &palaces);
		for(int j = 0; j < palaces; j++){
			scanf("%lld %lld", &row, &col);
			if((row % 2 == 0 && col % 2 != 0) || (row % 2 != 0 && col % 2 == 0)) wins ++;
		}
		if(wins % 2 != 0) printf("Ada\n");
		else printf("Vinit\n");
	}
	return 0;
}
