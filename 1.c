#include <stdio.h>
 
int main() {
	int i, a = 0, b = 0, soma = 0;
		
	for(i=1; i<1000; i++){
		a = i%3;
		b = i%5;
		if(a == 0 || b == 0){
			soma = soma+i;
		}
	}
	printf("%d", soma);
	
    return 0;
}
