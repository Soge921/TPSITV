from socket import AF_INET, SOCK_DGRAM, socket 

BUFFER_SIZE = 1024



HOST = "127.0.0.1"
PORT = 5000

def chatClient():
    with socket(AF_INET,SOCK_DGRAM) as s:
        user = input("inserire il tuo username:")
        user = user.encode('utf8')
        s.sendto(user, (HOST, PORT))
    while True: 
        with socket(AF_INET,SOCK_DGRAM) as s:
            msg =input("inserie messaggio:")
            msg = msg.encode('utf8')
            s.sendto(msg, (HOST, PORT))
            

    


    



if __name__ == "__main__":
    chatClient()