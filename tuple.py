s1 = (1,2,'s')
x = s1.count(1)
print(x)
print(s1.index('s'))

s3 = (20,)

print(isinstance(s3,tuple))

# 定义元组 -- 组包
t1 = (1,2,3)
#基础解包
a,b,c = t1

# 扩展解包(*) --收集剩余的元素,并且生成一个列表
x,*y = t1
*o,i = t1

