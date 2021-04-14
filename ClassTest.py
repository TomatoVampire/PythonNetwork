import sys


class Animal:
    name = ""

    def __init__(self, n="Animal"):
        self.name = n
    def setName(self,n):
        self.name = n

x = Animal("Cat")
x.setName("Cat")
print("创建的动物为：" + x.name)
# print(x.__class__)
