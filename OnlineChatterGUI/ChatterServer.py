from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #UDP
serverSocket.bind(('127.0.0.1', serverPort))
print('The server is ready to receive.')

userlist = {} # 用户列表(address，昵称)（字典）
addr = [] # address存储

def searchAddress(addre,  add ):
    if not add in addre:
        return False
    else:
        return True

def announce_to_all(addre, msg):
    # 发送给所有地址
    for add in addre:
        serverSocket.sendto(msg.encode(), add)

announce = ''

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    msg = message.decode()
    # print("client from:", clientAddress)
    if searchAddress(userlist, clientAddress):

        # 发送的为退出消息
        if msg == '_EXIT':
            announce = str(userlist[clientAddress]) + " has left the chat."
            del userlist[clientAddress]
        else:
            announce = str(userlist[clientAddress]) + ": " + msg
    else:
        if msg == "_EXIT":
            continue
        # 首次加入，消息为用户名
        addr.append(clientAddress)
        userlist[clientAddress] = message.decode()
        announce = msg + " has joined the chat. (ip = "+ str(clientAddress) +")"
    print(announce)
    announce_to_all(userlist, announce)
serverSocket.close()

