from socket import *
from threading import *
import time
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

# 接受服务端的通知
def receive_announce():
    while True:
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode())
        except:
            break
    # print("client program has ended")

# 等待输入信息发送给服务器
def input_message():
    while True:
        try:
            # message = input('(send)' + name + ': ')
            message = input()
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            # 退出聊天室
            if message == '_EXIT':
                print('left chat')
                time.sleep(0.5)
                clientSocket.close()
                break
        except:
            break


r = Thread(target=receive_announce, name='listenerThread')
t = Thread(target=input_message, name='inputThread')
r.start()
t.start()

r.join()
t.join()