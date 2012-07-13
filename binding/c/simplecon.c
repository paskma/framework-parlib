#import <stdio.h>
#import <string.h>

#define MAX_LINE 1024
char line_buf[MAX_LINE];
int buf_len = 0;
int pos = 0;
int last_return = -1;


static void prepare_line() {
	fgets(line_buf, MAX_LINE, stdin);
	pos = 0;
	buf_len = strlen(line_buf);
	
	if (buf_len > 0 && line_buf[buf_len-1] == '\n') {
		line_buf[buf_len-1] = '\0';
		buf_len -= 1;
	}
}

int simplecon_get_char() {
	if (last_return == -1) {
		prepare_line();
	}

	if (pos == buf_len) {
		last_return = -1;
		return last_return;
	}
	
	last_return = line_buf[pos++];
	return last_return;
}
