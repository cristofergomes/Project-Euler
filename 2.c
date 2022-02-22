#include <stdio.h>

int main(){
	
	int i, a = 1, b = 0, c = 2, par = 0, sobra = 0;
	
	while(b<=4000000){
		b = c + a;
		sobra = b%2;
		if(sobra == 0){
			par = par+b;	
		}		
		a = c;
		c = b;
	}
	par = par+2;
	printf("%d\n", par);
	
	return 0;
}
