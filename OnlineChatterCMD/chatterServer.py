from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #UDP
serverSocket.bind(('', serverPort))
print('The server is ready to receive.')

userlist = {} # 用户列表(address，昵称)（字典）
addr = [] # address存储

def searchAddress(addr,  add ):
    for temp in addr:
        if add == temp:
            return True
    return False

announce = ''

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    msg = message.decode()
    print("client from:", clientAddress)
    if searchAddress(addr, clientAddress):

        # 发送的为退出消息
        if msg == '_EXIT':
            del userlist[clientAddress]
            announce = userlist[clientAddress] + " has left the chat."
        else:
            announce = userlist[clientAddress] + ": " + msg
    else:
        # 首次加入，消息为用户名
        addr.append(clientAddress)
        userlist[clientAddress] = message.decode()
        announce = msg + " has joined the chat."
    print(announce)
serverSocket.close()
