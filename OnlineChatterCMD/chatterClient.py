from socket import *
# 服务器的参数
serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
serverPort = 12000
# ipv4网络 客户端端口号为自动分配
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 发送分组到上方填写的ip和端口处

name = input("please input client name: ")
print("welcome to the chatter, ", name)
print("help info: type any characters to send msg. Type '_EXIT' to leave the chat")
# 首次链接，给服务端发送用户名
clientSocket.sendto(name.encode(), (serverName, serverPort))

while True:
    message = input('Input chat content: ')
    # completeMsg = name + ": " + message
    # 发送给服务端的信息直接为输入的信息
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # 退出聊天室
    if message == '_EXIT':
        break
    # 等待接收分组。。。

    # 获取获得分组的信息及服务器ip（=serverName） 2048为buffer size(B)
    # modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # print(modifiedMessage.decode())
clientSocket.close()