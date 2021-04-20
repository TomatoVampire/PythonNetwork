from socket import *
serverName = 'localhost' # 127.0.0.1
serverPort = 12000
# 创建TCP链接
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP
clientSocket.connect((serverName, serverPort))
reqfile = input("please input file name: ")
# 发送下载请求
clientSocket.send(reqfile.encode())

fileMsg = clientSocket.recv(1024).decode()
print("Server message: ", fileMsg)

if fileMsg == "success":
    f = open("rec-"+reqfile, "wb")
    chunksize = 1024 # 1kb
    # 获取服务端信息
    while True:
        serverMsg = clientSocket.recv(chunksize)
        if serverMsg:
            # print("received chunk size: ", chunksize)
            f.write(serverMsg)
        else:
            break
else:
    pass
# 关闭连接
clientSocket.close()