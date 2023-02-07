import itertools as its

# 迭代器
words = "1234567890"

# 生成密码本的位数，八位数，repeat=8
r = its.product(words, repeat=8)

# 保存在文件中，追加
dic = open("E:/possword.txt", "a")


for i in r:
    dic.write("".join(i))                 # jion空格链接
    dic.write("".join("\n"))
    print(i)
dic.close()
print("密码本已生成")
