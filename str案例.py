#邮箱格式验证：验证邮箱格式(至少包含一个@和至少一个.)  --也可以使用 for ' ' in 字符串 来判断

while True:
    s = input("请输入您的邮箱: ")
    idx1 = s.count('@')
    idx2 = s.count('.')
    if idx1 == 1 and idx2 >= 1:
        print("邮箱格式正确")
        break
    else:
        print("邮箱格式错误")