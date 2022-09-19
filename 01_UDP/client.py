from ast import main
from socket import AF_INET, SOCK_DGRAM, socket 
BUFFER_SIZE = 1024
def letturaServer():
    host=input("inserire l'host:")
    port=int(input("inserire porta"))
    return host,port
def letturaUsername(HOST,PORT):

    with socket(AF_INET,SOCK_DGRAM) as s:
        user = input("inserire il tuo username:")
        user = user.encode('utf8')
        s.sendto(user, (HOST, PORT))
def chatClient(HOST,PORT):
    
    while True: 
        with socket(AF_INET,SOCK_DGRAM) as s:
            msg =input("inserie messaggio:")
            msg = msg.encode('utf8')
            s.sendto(msg, (HOST, PORT))                
def main():
    host,port= letturaServer()
    letturaUsername(host,port)
    chatClient(host,port)

if __name__ == "__main__":
    main()