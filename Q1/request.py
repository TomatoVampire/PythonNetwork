import os.path

import requests
import sys

# 用户输入网址
website = input("Please input a URL (start with 'http') : ")
r = requests.get(website, stream=True)

# 保存文件名
filename = "webpage.html"
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

# 获取文件大小
size = os.path.getsize(filename)

print("URL: " + website)
print("file name: " + filename)
print("file size: ", size, "B")