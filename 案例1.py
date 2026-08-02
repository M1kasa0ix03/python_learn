ant1 = "admin"
pas1 = "666888"
ant2 = "zhangsan"
pas2 = "123456"
ant3 = "taoge"
pas3 = "888666"

while True:
    ant = input("请输入你的账号：")
    pas = input("请输入你的密码：")
    if ant == "" or pas == "":
        print("输入的用户名和密码不能为空！请重新输入")
        continue
    if ant == ant1 and pas == pas1:
        print("登陆成功")
        break
    elif ant == ant2 and pas == pas2:
        print("登陆成功")
        break
    elif ant == ant3 and pas == pas3:
        print("登陆成功")
        break
    else:
        print("错误，请重新输入")

#小的登录代码块   
