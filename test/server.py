from socket import *
import sys

port = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', port))
print('UDP 服务端开始侦听')

user = {}   # map(ip, 昵称)

def sendToAll(user, msg):
    for addr in user:
        serverSocket.sendto(msg.encode(), addr)

while True:
    msg, addr = serverSocket.recvfrom(2048)
    msg = msg.decode()
    response = ''
    if msg == 'quit':   # 退出
        response = user[addr] + ' 退出了聊天室'
        del user[addr]
    elif not addr in user:  # 新加入
        user[addr] = msg.split('hello,')[1]
        response = user[addr] + ' 进入了聊天室'
    else:   # 正常消息
        response = user[addr] + ': ' + msg
    # 响应
    sendToAll(user, response)
    print(response)
