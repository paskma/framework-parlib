#include <stdio.h>
#include <string.h>

#include "simplenet.h"

int main() {
	int slotnumber;
	int c, counter;
	char buf[1024*1024];
	char *request;
	
	//slotnumber = simplenet_connect("www.super.cz", 80);
	slotnumber = simplenet_connect("www.google.cz", 80);
	if (slotnumber < 0) {
		printf("error connect %d", slotnumber);
		return 1;
	}
	
	request = "GET /\r\n";
	simplenet_write_buf(slotnumber, request, strlen(request));
	
	for(;;) {
		c = simplenet_read(slotnumber);
		if (c == -2) {
			printf("error read\n");
			return 1;
		}
		
		if (c == -1) {
			buf[counter++] = '\0';
			break;
		}
		
		buf[counter++] = (char)c;
	}
	
	printf("The file:\n%s\n", buf);
	
	simplenet_close(slotnumber);
	printf("Done.\n");
	return 0;
}
