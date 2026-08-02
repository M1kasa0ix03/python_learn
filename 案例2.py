import random
rd_num = random.randint(0,100)



while True:
    et = int(input("请输入一个数字: "))
    if et > rd_num :
        print("错误，猜大了")
        continue
    elif et < rd_num :
        print("错误，猜小了")
        continue
    else:
        print ("正确")
        break
print(f"猜的数字为：{et}")
# 猜数字游戏