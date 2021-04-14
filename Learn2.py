import sys
#输入
#强制类型转换
#guess = int(input("输入一个数字"))
'''
if guess == 1:
    print("猜对了！")
else:
    print("猜错了！")
'''
list = [1, 2, 3]
#for循环迭代
for a in list:
    pass#空语句
    print(a)
else:
    pass
    #print(a+2)
#迭代器iterator
i = iter(list)
print(next(i))#取本身，然后i++
for x in i:
    print(x, end=" ")
print("\n")

'''
函数:
以冒号标记开始，占一个缩进
返回值不需要在头写出
'''
def max(a, b=0):
    if a > b:
        return a
    else:
        return b
def hello():
    print("Hello world!")
maxx = max(a=5, b=13)
print(maxx)
hello()

def paratest(a):
    a=5
    print(id(a))
    return
a=1
print(id(a))
paratest(a)
print(id(a))
print(a)