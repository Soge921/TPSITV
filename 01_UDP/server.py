from socket import AF_INET, SOCK_DGRAM, socket 

BUFFER_SIZE = 1024


HOST = "0.0.0.0"
PORT = 5000

print("---STANZA PUBBLICA---")

def chatServer():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        data = s.recvfrom(BUFFER_SIZE)
        user = data[0].decode('utf8')
    
   
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        while True:
            data = s.recvfrom(BUFFER_SIZE)
            msg = data[0].decode('utf8')
            
            print(f"{user}:{msg}")

    


    



if __name__ == "__main__":
    chatServer()


