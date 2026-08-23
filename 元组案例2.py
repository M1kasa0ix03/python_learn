#学生成绩单系统
sdu = (
    ("s001","wangl",85,92,78),
    ("s002","li",92,88,95),
    ("s003","shi",78,85,82),
    ("s004","zeng",99,79,91),
    ("s005","zhou",95,96,89),
    ("s006","wangz",76,82,77),
    ("s007","hong",89,91,94),
    ("s008","xul",75,69,82),
    ("s009","xum",86,89,98),
    ("s010","xun",66,59,72)
)
# 1. 每个学生的总分与平均分（元组解包）
for sid, name, chinese, math, english in sdu:
    total = chinese + math + english          # 每个学生单独算，不累加
    avg = total / 3
    print(f"{sid},{name},{total},{avg:.1f}")
#在变量名后面加一个冒号加一个.1代表小数点一位，f代表浮点数形式

#2.最低与最高与平均（用 _ 占位忽略不需要的字段）
cs = [chinese for _, _, chinese, _, _ in sdu]

ms = [math for _, _, _, math, _ in sdu]

es = [english for _, _, _, _, english in sdu]

#获取列表

print(f"语文最低分：{min(cs)},最高分:{max(cs)},平均分：{sum(cs)/len(cs)}")
print(f"数学最低分：{min(ms)},最高分:{max(ms)},平均分：{sum(ms)/len(ms)}")
print(f"英语最低分：{min(es)},最高分:{max(es)},平均分：{sum(es)/len(es)}")

#查找平均分大于90的学生
print("优秀学生如下")
for sid, name, chinese, math, english in sdu:
    avg = (chinese + math + english) / 3
    if avg > 90:
        print(f"学号:{sid},学生：{name},平均分:{avg:.1f}")