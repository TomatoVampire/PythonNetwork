from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 任何发送到这个ip这个端口的分组都是由此套接字接收
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    # 收到分组的客户端的信息和IP
    message, clientAddress = serverSocket.recvfrom(2048)
    print("client from:", clientAddress)
    # upper()转成大写
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
