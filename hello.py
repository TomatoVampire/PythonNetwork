import sys
# welcome to Python!
'''
注释1
'''
"""
注释2
"""
print("Hello world!")
print("Nice to meet:")
#多行代码放入一行内
a = 1 + \
    1
#获取用户输入
#a = input("please input a number:\n")
if a == 1:
    print("Alice")
elif a == 2:
    print("Bob")
else :
    print("Nobody")
it = 0
#while循环
while it<5 :
    a += 1
    it+=1
#跳出循环时
else:
    a += 2;
print(hex(a))

#字符串（不可变）
s = "welcome!"
#多行字符
s = """
nice to
meet you!
"""
#输出不换行
print(s, end=" ")
#删除对象
del s
#列表
lis = [1, 2, 3, "4"]
#集合
se1 = {1,2,"3"}
se2 = {1,2,"4"}
se3 = set()#空集合
print(se1 & se2)#交集&并集|异或^
#字典（map）
dic = {(1,"a"), (2, "b")}
dic2 = {}

