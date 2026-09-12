#案例1
#商品货架用字典中值嵌套字典来实现

shopcart  = {}

str1 = """
######  购物车系统 ######
#      1.添加购物车     #
#      2.修改购物车     #
#      3.删除购物车     #
#      4.查询购物车     #
#      5.退出购物车     #

#########################

"""
while True :
    print(str1)
    # 用户执行操作
    choice = input("请选择要执行的操作(1-5):")
    match choice:
        case "1":
            good_name = input("请输入商品的名称:")
            good_price = float(input("请输入商品的价格："))
            good_nums = int(input("请输入商品的数量"))
            if good_name in shopcart :
                print("该商品已经存在，请重新选择")
            else :
                 shopcart[good_name] = {"price" : good_price,"nums" : good_nums}
                 print("商品添加完毕")
        case "2":
            xname = input("请输入你要修改的名称：")
            xprice = float(input("请输入你要修改的价格："))
            xnums = int(input("请输入你要修改的数量："))
            if xname not in shopcart :
                print("不存在，请再次选择")
            else:     
                shopcart[xname] = {"price" : xprice,"nums" :xnums }
        case "3":
            dname = input("请输入你要删除商品的名称：")
            if dname in shopcart :
                del shopcart[dname]
                print("删除完毕")
            else :
                print("不存在,请重新选择")
        case "4":
            fname = input("请输入你要查查询的商品的名称")
            if fname not in shopcart :
                print("不存在，请再次输入")
            else:
                good_info = shopcart[fname]
                print(f"商品价格:{good_info['price']},商品数量:{good_info['nums']}")
        case "5":
            print("您已经退出购物车")
            break
        case _ :
            print("非法操作，不支持!!!")

