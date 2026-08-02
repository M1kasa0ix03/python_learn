s = []
for i in range(0,10):
    x = int(input("输入一个有效的数字"))
    s.append(x)
s.sort()
print(s[-1])
print(s[0])
print("平均值: ",sum(s)/len(s))

