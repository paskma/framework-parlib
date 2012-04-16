

int simplenet_connect(const char * hostname, int port);
int simplenet_read(int slotnumber);
int simplenet_close(int slotnumber);
int simplenet_write_buf(int slotnumber, const char * buf, int size);
int simplenet_write_char(int slotnumber, int character);
int simplenet_flush(int slotnumber);
int simplenet_set_timeout(int slotnumber, int timeoutmillis);
