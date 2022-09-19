from socket import AF_INET, SOCK_DGRAM, socket 
BUFFER_SIZE = 1024
def letturaServer():
    host=input("inserire l'host:")
    port=int(input("inserire porta"))
    return host,port
def chatServer(HOST,PORT):
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
def main():
    print("---STANZA PUBBLICA---")
    host,port = letturaServer()
    chatServer(host,port)

if __name__ == "__main__":
    main()


