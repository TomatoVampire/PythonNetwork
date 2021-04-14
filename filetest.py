import sys
'''
f = open("test.txt", "w")
f.write("hello world!\n")
f.write("nice to meet you!")
f.close()
'''
f = open("test.txt", "r")
str = f.readline()
print(str)