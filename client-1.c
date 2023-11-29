#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <stdlib.h>
#include <strings.h>
#include <unistd.h>

void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;

    struct sockaddr_in serv_addr;
    struct hostent *server; 
/*The hostent structure is used by functions to store information about a given host, such as host name, IPv4 address, and so forth*/
    char buffer[1001];

    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }

    portno = atoi(argv[2]);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    if (sockfd < 0) 
        error("ERROR opening socket");

    server = gethostbyname(argv[1]);
    /* gethostname() system call returns a null-terminated hostname*/

    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }

    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);

    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR connecting");

    do{
        printf("Please enter the message: ");
        bzero(buffer, 256);
        fgets(buffer, 255, stdin);
        int testBuffer = strcmp(buffer, "quit");

        n = write(sockfd, buffer, strlen(buffer));

        if (n < 0) 
            error("ERROR writing to socket");

        bzero(buffer, 256);

        n = read(sockfd, buffer, 255);

        if (n < 0) 
            error("ERROR reading from socket");

        printf("%s\n",buffer);

        if(testBuffer == 10){
            exit(1);
        }

    }while(strcmp(buffer, "quit") != 10);

    return 0;
}
