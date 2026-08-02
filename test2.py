
s = int(input("输入一个值："))
x = 1
while s > 0 :
    s -= 1
    print("python")
else:
    print("打印结束")

sum = 0
while x <= 100:
    if x % 2 == 0:
        sum += x
    x += 1

print(f"累加之和为{sum}")
    
stt = input("输入一个变量：")
for s in stt :
    print(s)
else:
    print("结束")

ant = 0
for i in range(1,101,3):
    ant += i
print(ant)

m = int(input("请输入m行:"))
n = int(input("请输入n列:"))

for i in range(0,m) :
    for j in range(0,n):
        print("*",end = "  ")
    print()    
else:
    print("打印完了")

for i in range(1,m+1):
    for j in range(1,i+1) :
        print(f"{j} x {i} = ",j * i,end = "\t")
    print()
