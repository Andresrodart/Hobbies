#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
#ifdef _WIN32
#include <fcntl.h>
#endif

int64_t busquedaBinaria ( std::deque<int64_t> arreglo, int64_t objetivo ) {
	int64_t puntoMenor;
	int64_t puntoMedio;
	int64_t puntoFinal;
	while(puntoMenor < puntoFinal){
		puntoMedio = (puntoFinal+puntoMenor)/2;
		if(arreglo[puntoMedio] == objetivo){
			return puntoMedio;
		}else if(arreglo[puntoMedio] > objetivo){
			puntoFinal = puntoMedio-1;
		}else{
			puntoMenor = puntoMedio+1;
		}
	}
}