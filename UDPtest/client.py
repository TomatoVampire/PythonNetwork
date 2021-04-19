from socket import *

# 服务器的参数
serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
serverPort = 12000
# ipv4网络 客户端端口号为自动分配
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 发送分组到上方填写的ip和端口处
while True:
    message = input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # 等待接收分组。。。

    # 获取获得分组的信息及服务器ip（=serverName） 2048为buffer size(B)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(modifiedMessage.decode())
clientSocket.close()