from tkinter import *
import time
from threading import *
from socket import *

class Window:
    def __init__(self, master):
        self.hasleft = False
        self.isnamesent = False
        self.master = master
        self.master.title('TomatoChat by 2018172020')
        self.name=''

        self.frame = Frame(self.master, bg='#AFEEEE')
        self.frame.pack(expand=True, fill=BOTH)

        self.titlestr = StringVar()
        self.titlestr.set("TomatoChat")
        self.label = Label(self.frame, font=('Arial', 13), textvariable=self.titlestr, bg='#FA9072')# text="TomatoChat")
        self.label.pack()

        # 滑轨
        self.scroll = Scrollbar(self.frame, orient=VERTICAL)
        self.scroll.pack(side=RIGHT, fill=BOTH)

        # 聊天窗口
        self.text = Text(self.frame, undo=True, height=20, width=50, yscrollcommand=self.scroll.set)
        self.text.pack(expand=True, fill=BOTH)
        self.text.insert("1.0", "Welcome to TomatoChat! Please input your name: \n")
        self.scroll.config(command=self.text.yview)

        # 输入窗口
        self.inputtext = Text(self.frame, undo=True, height=10, width=70)
        self.inputtext.pack(expand=True, fill=BOTH)
        self.inputtext.insert("1.0", "Please input your name here")

        self.button = Button(self.frame, text='send!', width=5, height=1, command=self.send_msg)
        # 只要加入按钮的command就无法接收和显示消息？？？？
        self.button.pack()

        self.serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
        self.serverPort = 12000
        # ipv4网络 客户端端口号为自动分配
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.clientSocket.sendto('test'.encode(), (self.serverName, self.serverPort))


    def receive_announce(self):
        while True:
            try:
                modifiedMessage, serverAddress = self.clientSocket.recvfrom(2048)
                print(modifiedMessage.decode())
                self.text.insert("end", modifiedMessage.decode()+'\n')
            except:
                break
        # print("client program has ended")

    # 等待输入信息发送给服务器

    def close(self):
        self.clientSocket.sendto("_EXIT".encode(), (self.serverName, self.serverPort))

    def send_msg(self):
        msg = self.inputtext.get("1.0", "end - 1 chars")
        if msg == "":
            return
        if not self.hasleft:
            self.clientSocket.sendto(msg.encode(), (self.serverName, self.serverPort))
        self.inputtext.delete('1.0', 'end')
        if not self.isnamesent:
            self.titlestr.set("Welcome, "+ msg + " !")
            self.name = msg
            self.isnamesent = True
        elif msg == '_EXIT':
            self.titlestr.set("Bye, " + self.name + " !")
            self.text.insert("end", "You have left TomatoChat. Goodbye!")
            self.hasleft = True

root = Tk()
window = Window(root)

r = Thread(target=window.receive_announce, name='listenerThread')
r.start()

# r.join()

root.mainloop()
window.close()