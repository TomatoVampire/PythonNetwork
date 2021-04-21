import tkinter as tk
import time
from threading import *
from socket import *

class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.label = tk.Label(self.frame, text="My NotePad")
        self.label.pack()

        self.text = tk.Text(self.frame, undo=True, height=20, width=70)
        self.text.pack(expand=True, fill=tk.BOTH)
        self.text.insert("1.0", "hiii")
        self.button = tk.Button(self.frame, text='send', width=5, height=1)#, command=self.send_msg)
        self.button.pack()

        self.serverName = 'localhost' # 会自动查询DNS获得域名的ip（localhost = 127.0.0.1）
        self.serverPort = 12000
        # ipv4网络 客户端端口号为自动分配
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.clientSocket.sendto('testcode'.encode(), (self.serverName, self.serverPort))


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
'''
    def send_msg(self):
        msg = self.text.get("1.0", "end - 1 chars")
        self.clientSocket.sendto(msg.encode(), (self.serverName, self.serverPort))
'''

root = tk.Tk()
window = Window(root)

r = Thread(target=window.receive_announce, name='listenerThread')
r.start()

# r.join()

root.mainloop()
window.close()