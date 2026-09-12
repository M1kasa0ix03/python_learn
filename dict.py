ars = { "kai": 29,"ode":8,"saka" : 7}
print(ars)
print(ars["kai"])
print(f"哈夫茨的号码是{ars['kai']}")
ars.get("saka")
print(ars.keys())
print(ars.values())
print(ars.items())
s1 = ars.pop("saka") #删除并且返回值
del ars["ode"]
print(f"已经删除的为{s1}")
print(ars.items())
#遍历
for k in ars.keys() :
    print(f"{k}:{ars[k]}")
for item in ars.items():
    print(f"{item[0]}:{item[1]}")
#解包方法