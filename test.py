print("hello")
# 注释
print(100)
print(True) #布尔类型
print(False)
print(None)#空值
print(True + 1)

num = 111
print(num)
nm = "havertz"
print(nm)
num = "ok"
print(num)

print(num,nm)


kkk,kk1 = 29,7
print(kkk,kk1)

a = 10
b = 20
print(a,b)
c = a
a  = b
b = c
print(a,b)
print(type(c))
print(type(num))

print(isinstance(num,int))

s1 = """
你好
   你好
      你好
"""
print(s1)


ss ="1" + "2"

print(s1 + ss + "1")


sc = 1
sc1 = 2
sc2 = 3
print("我是%s" %sc)
print("woshi %s he %s he %s"%(sc,sc1,sc2))

print(f"wooshi {sc} he{sc1} he{sc2}")




s = input("请输入您的年龄：")
print(f"您的年龄{s}岁")


x = float(input("请输入x的值:" ))
y = float(input("请输入y的值:" ))

print(f"{x} > {y}",x > y)

s = float(input("请输入一个值:"))
print(f"{s}在10-20之间:",10<= s <=20)
print(f"{s}在10-20之间:",s >=10 and s<=20)


sccc11 = 1111
if sccc11 > 200:
   print("easy")  

acnt_ = "2371313638"
pas_ = "cjhcjhcjhcjh"
acnt = input("请输入你的账号：")
pas = input("请输入你的密码：")
if acnt == acnt_ and pas == pas_ :
   print("密码正确")
else:
   print("密码错误")