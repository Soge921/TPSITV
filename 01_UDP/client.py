from socket import AF_INET, SOCK_DGRAM, socket 

BUFFER_SIZE = 1024


HOST = "192.168.95.255"
PORT = 5000

def chatClient():
    while True:
        with socket(AF_INET,SOCK_DGRAM) as s:
            msg =input("inserie messaggio:")
            msg = msg.encode('utf8')
            s.sendto(msg,(HOST,PORT))

    


    



if __name__ == "__main__":
    chatClient()