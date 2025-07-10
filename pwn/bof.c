#include<stdio.h>

void win() {
	puts("Called win() function");
}

int main(){
	char buf[32];
	printf("Gimme some text:\n");
	gets(buf);
	return 0;
}