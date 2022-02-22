#include <stdio.h>

int main(){
	
	long long int fator, primo, num, teste, cont, teste2;
	int i, j;
		
	num = 600851475143;
	printf("Maior fator primo de %lld\n", num);
	for(i = 2; i < num; i++){
		teste = num%i;
		if(teste == 0){
			fator = num/i;
			cont = 0;
			for(j = 2; j < fator; j++){
				teste2 = fator%j;
				if(teste2 == 0){
					cont = cont+1;
					if(cont > 0){
						break;
					}
				}
			}
			if(cont == 0){
				primo = fator;
				printf("%lld\n", primo);
				break;
			}
		}
	}
		
	return 0;
}
