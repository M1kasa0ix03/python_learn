s = [1,2,3,4,"123"]

#获取
print(s[0])
print(s[-5])
print(s[-1])

#修改

s[0] = 3
s[-1] = True
print(s[0])
print(s[-1])

#删除
print(s)
del s[3]
print(s)
#遍历
for i in s:
    print(i)

#切片的操作
s1 = s[0:3:1]
print(s1)
print(s[:4:1])
print(s[:4:])
print(s[:4])

#增删改查
