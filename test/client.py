from socket import *
import sys
import threading
import time

# 监听线程
class listener(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        while True:
            try:    # 利用 conn.close 作为退出标志
                msg, addr = self.conn.recvfrom(2048)
                print(msg.decode())
            except:
                break

# 发送线程
class sender(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
    def run(self):
        while True:
            msg = input()
            self.conn.sendto(msg.encode(), self.addr)
            if msg == 'quit':
                time.sleep(0.5)     # 防止管道过早关闭
                self.conn.close()
                break

nickname = sys.argv[3]
addr = (sys.argv[1], int(sys.argv[2]))
conn = socket(AF_INET, SOCK_DGRAM)
conn.sendto(('hello,'+nickname).encode(), addr)

l = listener(conn)
s = sender(conn, addr)

l.start()
s.start()

l.join()
s.join()
