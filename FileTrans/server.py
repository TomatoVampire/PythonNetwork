from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)
print("server ready to connect.")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("----------------------")
    print("connect client: ", addr)
    filename = connectionSocket.recv(1024).decode()
    print("requested file: ", filename)
    content = None
    try:
        f = open(filename, "rb")
        content = f.read()
        f.close()
        connectionSocket.send("success".encode())
    except:
        print("ERROR: file not found")
        connectionSocket.send("fail".encode())
    if content:
        # print("send content...")
        connectionSocket.send(content)
        connectionSocket.close()
serverSocket.close()