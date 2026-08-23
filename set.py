#定义空集合
s1 = set()
print(type(s1))
#定义一个集合
s2 = {2,2,3,4,4,5,6,7,7,7,9,0,0}
print(s2)
s2.add(10)
s2.pop()
print(s2)
s3 = {1,2,3,4,5,6,7,8,10,22,33}

s4 = s2.union(s3)
s5 = s2.intersection(s3)
s6 = s2.difference(s3)
s7 = s3.difference(s2)
print(s4)
print(s5)
print(s6)
print(s7)