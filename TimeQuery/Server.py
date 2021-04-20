
'''
实现一个基于客户服务器的系统时间查询程序。传输层使用 TCP 。
交互过程：
1)客户端向服务器端 发送字符串 ” 。
2)服务器端收到该字符串后，返回当前系统时间。
3)客户端向服务器端发送字符串 ” 。
4)服务器端返回 ” Bye”，然后结束 TCP 连接。

'''
from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
#print(time.asctime(time.localtime(time.time())))
# 来自客户的最大连接请求为?
serverSocket.listen(10)
print("server ready to connect.")

while True:
    print("------------------------------")
    #print("Start a new listen")
    connectionSocket, addr = serverSocket.accept()
    print("New server: ", addr)
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == 'Time':
            timeMsg = time.asctime(time.localtime(time.time()))
            # print("received msg: ", sentence)
            connectionSocket.send(timeMsg.encode())
        elif sentence == 'Exit':
            exitMsg = "Bye"
            connectionSocket.send(exitMsg.encode())
            connectionSocket.close()
            break
        elif sentence == '':
            connectionSocket.send("Please input a command! ".encode())
        else:
            connectionSocket.send("Error! Command not found.".encode())
            # print("Error! Command not found.")
