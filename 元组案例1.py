# 两个变量值交换
a =10
b = 30   
a,b = b,a
#等号右边是定义元组，相当于组包的操作
#等号左边是解包的操作
print(a)
print(b)
a = 100
b = 200
#三个变量值交换
c = 300
c,b,a = a,b,c
print(a)
print(b)
print(c)
