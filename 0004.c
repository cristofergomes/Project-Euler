#include <stdio.h>

int main(){
	
	int i, j, num, maior = 0;
	int a, b, c, x, y, z;
	
//  320*314 = 100480 e 999*999 = 998001
//  grandes chances do maior palindromo ter 6 digitos
//  numero de 6 digitos (xxxxxx) --> (abcxyz)
//  nesse caso a=z b=y e c=x para ser palindromo
	
	for(i=320; i<=999; i++){
		for(j=314; j<=999; j++){
			num = i*j;
			z = num%10;
			a = num/100000;
			if(a == z){
				y = num/10;
				y = y%10;
				b = num/10000;
				b = b%10;
				if(b == y){
					x = num/100;
					x = x%10;
					c = num/1000;
					c = c%10;
					if(c == x){
						if(num > maior){
							maior = num;
							printf("%d\n", maior);
						}
					}
					
				}
			}
		}		
	}
	return 0;
}
