from socket import *
'''
▪ 实现一个基于客户/服务器的网络文件传输程序。
▪ 传输层使用TCP。
▪ 交互过程
1) 客户端从用户输入获得待请求的文件名。
2) 客户端向服务器端发送文件名。
3) 服务器端收到文件名后，传输文件。
4) 客户端接收文件，重命名并存储在硬盘。
'''
serverName = 'localhost' # 127.0.0.1
serverPort = 12000
# 创建TCP链接
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP
clientSocket.connect((serverName, serverPort))
reqfile = input("please input file name: ")
# 发送下载请求
clientSocket.send(reqfile.encode())

# 获取服务端信息
serverMsg = clientSocket.recv(1024)
if serverMsg:
    with open("rec-"+reqfile, "wb") as f:
        f.write(serverMsg)
'''
decodeMsg = serverMsg.decode()
if decodeMsg == "Success":
    # 成功获取文件，开始下载
    file = open("testfile.txt", "wb")
elif decodeMsg == "Fail":
    # 获取失败
    print("Fail to download file, please retry. ")
'''
# 关闭连接
clientSocket.close()