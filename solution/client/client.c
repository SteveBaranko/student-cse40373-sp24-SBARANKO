#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <zmq.h>


int main(){
    void *context = zmq_ctx_new();
    void *requester = zmq_socket(context, ZMQ_REQ);

    int rc = zmq_connect(requester, "tcp://localhost:40639");
    if(rc == 0){
      printf("Successfully connected\n");
    }else{
      printf("Connection failed\n");
      exit(-1);
    }

    char buffer[256];
    // zero out the buffer
    memset(buffer, 0, 256);

    char response[250];
    // zero out the buffer
    memset(response, 0, 256);

    while(1){
        printf("Enter a valid beacon name: ");
        scanf("%s", buffer);
        if(strcmp(buffer, "exit") == 0){
          break;
        }
      
        //clean trailing newline and whatever else
        for( int i = 0; i < 256; i++){

          /////////////if whitsepace//////////
          if(buffer[i] == '\n' || buffer[i] == '\r' 
          || buffer[i] == '\t' || buffer[i] == '\v' 
          || buffer[i] == '\f'){
            ///////////endif///////////////////
          
          buffer[i] = '\0';//replace with null
          }
        }
      
        zmq_send(requester, buffer, 256, 0);
      

        if(zmq_recv(requester, response, 256, 0) > 0){
          printf("Received: %s\n", response);
        }else if(zmq_recv(requester, response, 256, 0) == -1){
          printf("Error\n");
        }
        else{
          printf("No response\n");
        }
    }

    zmq_close(requester);
    zmq_ctx_destroy(context);

  exit(0);
}