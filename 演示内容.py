# 将演示文档的文件内容打印出来

with open('./演示.txt', 'r') as f:# 用with open语句打开文件，并将文件对象赋值给变量f
    # 用read()方法读取文件内容并打印出来

    print(f.read())