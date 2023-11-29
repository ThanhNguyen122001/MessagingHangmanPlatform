
/*This code includes modfied code from a previous lab from GVSU CIS 457 Vijay Bhuse*/
//Thanh Nguyen, Isaac Bouwkamp
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <strings.h>
#include <unistd.h>

void error(char *msg){
	perror(msg);
	exit(1);
}
int main(int argc, char *argv[]){
	int sockfd, newsockfd, portno, clilen;
	char buffer[1000];//256

	struct sockaddr_in serv_addr, cli_addr;int n;
	if (argc < 2) {fprintf(stderr,"ERROR, no port provided\n");
		exit(1);
	}
		sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0)error("ERROR opening socket");
	bzero((char *) &serv_addr, sizeof(serv_addr));
	/* erases the data in the n bytes of the memory*/
	portno = atoi(argv[1]);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(portno);
	/* Host to net byte order for short int*/
	if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)error("ERROR on binding");
	listen(sockfd,5);/* 5 outstanding connections*/ 
	//listen(sockfd,5);/* 5 outstanding connections*/
	clilen = sizeof(cli_addr);
	int k = 0;
	while(k == 0){
		newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
		if (newsockfd < 0)error("ERROR on accept");
		bzero(buffer,1000);//256
		n = read(newsockfd, buffer, 999);//255
		if (n < 0) error("ERROR reading from socket");
		printf("Here is the message: %s\n",buffer);//buffer is the variable that will be reading in the value from the users

		int count = 0;
		char wordToGuess = {'H', 'E', 'L'};
		int wordLength = strlen(wordToGuess);
		printf("Word length: %d", wordLength);

		/*if (count < 1){
			//set this as the word that the players will try to guess.
			wordToGuess[1000] = buffer;
			count++;
		}*/
		
		/*for(int i = 0; i < 1000; i++){
			if( wordToGuess[i] == '\0'){
			
			}
		}*/
		

		n = write(newsockfd, "I got your message", 18);
		if (n < 0) error("ERROR writing to socket");
	}
	return 0;
}
