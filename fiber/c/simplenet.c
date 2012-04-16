#include <stdlib.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>


#define NSLOTS 256
#define EMPTY_SLOT -1

typedef int slot_t;

slot_t* slots = NULL;

static void check_and_init() {
int i;
	if (slots == NULL) {
		slots = (slot_t*) malloc(NSLOTS*sizeof(slot_t));
		for (i = 0; i < NSLOTS; i++) {
			slots[i] = EMPTY_SLOT;
		}
	}	
}

static int find_empty_slot() {
	int i;
	for (i = 0; i < NSLOTS; i++) {
		if (slots[i] == EMPTY_SLOT)
			return i;
	}
	return -1;
}

/// returns slotnumber or negative error code
int simplenet_connect(const char * hostname, int port) {
	int sockfd;
    struct hostent *server;
    struct sockaddr_in serv_addr;
    int result;

	check_and_init();	
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd == -1)
		return -1;
	
	server = gethostbyname(hostname);
	if (server == NULL)
		return -2;
	
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
    memcpy(&serv_addr.sin_addr.s_addr, server->h_addr, server->h_length);
    serv_addr.sin_port = htons(port);
    
    if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
    	return -3;
    
    result = find_empty_slot();
    if (result == -1)
    	return -4;
    
    slots[result] = sockfd;
    return result;
}

/// returns a byte from socket, -1 on end of file, -2 on error
int simplenet_read(int slotnumber) {
	int len;
	unsigned char buf;
	check_and_init();
	len = read(slots[slotnumber], &buf, 1);
	if (len == -1)
		return -2;
	if (len == 0)
		return -1;
	
	return buf;	
}

int simplenet_write_buf(int slotnumber, const char * buf, int size) {
	check_and_init();
	return write(slots[slotnumber], buf, size);
}

int simplenet_write_char(int slotnumber, int character) {
	char c = (char)character;
	return simplenet_write_buf(slotnumber, &c, 1);
}

int simplenet_flush(int slotnumber) {
	return fsync(slots[slotnumber]);
}

// returns 0 on success, -1 on error
int simplenet_close(int slotnumber) {
	int suc;
	check_and_init();
	suc = close(slots[slotnumber]);
	if (suc == 0) {
		slots[slotnumber] = EMPTY_SLOT;
		return 0;
	}
	
	return -1;
}

int simplenet_set_timeout(int slotnumber, int timeoutmillis) {
	struct timeval timeout;
	int sockfd;
	int suc;
	
	check_and_init();
	sockfd = slots[slotnumber];

	timeout.tv_sec = timeoutmillis / 1000;
	timeout.tv_usec = (timeoutmillis % 1000) * 1000;
    
    suc = setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, (void*)&timeout, sizeof(timeout));
    
    if (suc != 0)
    	return -1;
    
    suc = setsockopt(sockfd, SOL_SOCKET, SO_SNDTIMEO, (void*)&timeout, sizeof(timeout));
    
    if (suc != 0)
    	return -2;
    
    return 0;
}









