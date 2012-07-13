#include "stdio.h"

#include "simplecon.h"


int main() {
	int i;
	int c;
	char buf[1024];

	for (;;) {
		printf("Asking for line:\n");
		for (i = 0; ; i++) {
			c = simplecon_get_char();
			if (c == -1) {
				buf[i] = '\0';
				break;
			}
			
			buf[i] = (char)c;
		}
		
		printf("The line is '%s'\n", buf);
	}
}
