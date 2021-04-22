from socket import *
from threading import *
import time
# 服务器的参数
class Connect:
    def __init__(self):
        self.serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
        self.serverPort = 12000
        # ipv4网络 客户端端口号为自动分配
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        # 发送分组到上方填写的ip和端口处

        name = input("please input client name: ")
        print("welcome to the chatter, ", name)
        print("help info: type any characters to send msg. Type '_EXIT' to leave the chat")
        # 首次链接，给服务端发送用户名
        self.clientSocket.sendto(name.encode(), (self.serverName, self.serverPort))

    # 接受服务端的通知
    def receive_announce(self):
        while True:
            try:
                modifiedMessage, serverAddress = self.clientSocket.recvfrom(2048)
                print(modifiedMessage.decode())
            except:
                break
        # print("client program has ended")

    # 等待输入信息发送给服务器
    def input_message(self):
        while True:
            try:
                # message = input('(send)' + name + ': ')
                message = input()
                self.clientSocket.sendto(message.encode(), (self.serverName, self.serverPort))
                # 退出聊天室
                if message == '_EXIT':
                    print('left chat')
                    time.sleep(0.5)
                    self.clientSocket.close()
                    break
            except:
                break

    def close(self):
        self.clientSocket.sendto("_EXIT".encode(), (self.serverName, self.serverPort))

c = Connect()
r = Thread(target=c.receive_announce, name='listenerThread')
t = Thread(target=c.input_message, name='inputThread')

t.start()
r.start()

r.join()
t.join()

c.close()