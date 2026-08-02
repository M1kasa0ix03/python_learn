#生成1-20的平方列表  range(1,21)
s  = []
#传统方式
for i in range(1,21):
    s.append(i**2)
print(s)
#列表推导式
s1 = [i**2 for i in range(1,21)]
print(s1)


#案例2:从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表
ns = [22,33,44,12,92,32,99,654]
ns1 = [i**2 for i in ns if i % 2 == 0]
print(ns1)