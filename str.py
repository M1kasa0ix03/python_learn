s = "ai agent"
for i in s:
    print(i)

#切片
print(s[:8])
print(s[:8:2])

print(s[-1:-9:-1])

#常用方法
index = s.find('g')
print(index)

print(s.count('a'))

print(s.upper())

print(s.lower())
#默认空格
s_list = s.split()
print(s_list)
s_list1 = s.split("-")
print(s_list1)

#默认去除两端的空白
s_list3 = s.strip()
print(s_list3)
s_list4 = s.strip('a')
print(s_list4)


s1 = s.replace('a','A')
print(s1)

print(s.startswith("a"))