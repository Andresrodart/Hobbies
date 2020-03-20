#include <stdio.h>
#define ll long long 
int main(int argc, char const *argv[]){
	ll cases, wins, palaces, row, col;
	scanf("%lld", &cases);
	for(int i = 0; i < cases; i++){
		wins = 0;
		scanf("%lld", &palaces);
		for(int j = 0; j < palaces; j++){
			scanf("%lld %lld", &col, &row);
			if(!(row % 3 == 0 && col % 3 == 0) && !(row % 3 == 2 && col % 3 == 1) && !(row % 3 == 1 && col % 3 == 2)) wins ++;
		}
		if(wins % 2 != 0) printf("Ada\n");
		else printf("Vinit\n");
	}
	return 0;
}
