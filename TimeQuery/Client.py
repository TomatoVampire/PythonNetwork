from socket import *
'''
实现一个基于客户服务器的系统时间查询程序。传输层使用 TCP 。
交互过程：
1)客户端向服务器端 发送字符串 ”Time 。
2)服务器端收到该字符串后，返回当前系统时间。
3)客户端向服务器端发送字符串 ”Exit 。
4)服务器端返回 ” Bye”，然后结束 TCP 连接。
'''

serverName = 'localhost' # 127.0.0.1
serverPort = 12000
# 创建TCP链接
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP
clientSocket.connect((serverName, serverPort))
while True:
    message = input("please input command: ")
    # 发送信息
    clientSocket.send(message.encode())
    # 接受服务端的信息
    serverMsg = clientSocket.recv(1024)
    decodeMsg = serverMsg.decode()
    print("From server: {}".format(decodeMsg))
    if decodeMsg == "Bye":
        break
clientSocket.close()