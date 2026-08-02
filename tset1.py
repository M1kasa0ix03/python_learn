
s1 = int(input("请输入年份:"))

if s1 % 100 != 0 :
    if s1 % 4 == 0:
        print("是闰年")
    else:
        print("是平年")
else: 
    if s1 % 400 == 0:
        print("是闰年")
    else:
        print("是平年")

#小计算器
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字: "))
oper  = input("请输入运算符+ - * /: ")
match oper:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b} ")
    case "/" if b != 0:
        print(f"{a} / {b} = {a / b}")
    case _:
        print("输入的运算符错误")