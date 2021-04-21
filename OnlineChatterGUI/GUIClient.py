from tkinter import *
import time
from threading import *
from socket import *

class Window:
    def __init__(self, master):
        self.top = root
        self.top.title('TomatoChat: Client')
        self.top.geometry('500x500')

        mainframe = Frame(self.top)
        mainframe.pack()

        frame1 = Frame(mainframe).pack(side='top')
        frame2 = Frame(mainframe).pack()
        frame3 = Frame(mainframe).pack(side='bottom')
        # frame4 = Frame(mainframe) # ??

        # 欢迎信息
        welcometext = Label(frame1, text="Welcome to TomatoChat! ", bg='green', fg='white', font=('Consolas', 12), width=30).pack(side='top')

        # 消息板
        radioscroll = Scrollbar(frame1, orient=VERTICAL)
        radioscroll.pack(side=RIGHT, fill=BOTH)
        radiostr = StringVar()
        radiostr.set('hello!')
        self.radiotext = Text(frame1, bg='orange', fg='black', font=('Consolas', 10),
                         width=45, height=20,
                          wrap=NONE,
                         yscrollcommand=radioscroll.set
                         )
        self.radiotext.insert(INSERT, "This is some Sample Data \nThis is Line 2 of the Sample Data\n")
        self.radiotext.insert("end", "hellooooo")
        self.radiotext.pack(expand=True)
        radioscroll.config(command=self.radiotext.yview)
        sendbutton = Button(frame3, text='send', width=5, height=1, command=self.send_msg)
        sendbutton.pack(side='bottom')
        self.inputtext = Text(frame3, width=50, height=5)
        self.inputtext.pack(side='bottom')


        self.serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
        self.serverPort = 12000
        # ipv4网络 客户端端口号为自动分配
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        # self.clientSocket.sendto('testcode'.encode(), (self.serverName, self.serverPort))

    def send_msg(self):
        msg = self.inputtext.get("1.0", "end - 1 chars")
        self.radiotext.insert(END, msg)
        self.clientSocket.sendto(msg.encode(), (self.serverName, self.serverPort))

    def receive_announce(self):
        while True:
            try:
                print("waiting for msg...")
                modifiedMessage, serverAddress = self.clientSocket.recvfrom(2048)
                print(modifiedMessage.decode())
            except:
                break
        # print("client program has ended")

    # 等待输入信息发送给服务器

    def close(self):
        self.clientSocket.sendto("_EXIT".encode(), (self.serverName, self.serverPort))


root = Tk()
window = Window(root)

r = Thread(target=window.receive_announce, name='listenerThread')
r.start()

r.join()

root.mainloop()
window.close()