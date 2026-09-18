# 教务系统管理  这是一个类  学生也是一个类
class Student : 
    def __init__(self,name,chinese,math,english):
        self.name = name 
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名:{self.name},语文：{self.chinese},数学：{self.math},英语:{self.english}"
    #  初始值设为0，可以输入时只输入单科成绩等
    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None :
            self.chinese  = chinese
        if math is not None :
            self.math  = math   
        if chinese is not None :
            self.english  = english
    def remove_score(self):
        if self.chinese is not None :
            self.chinese = None
        if self.math is not None :
            self.math = None
        if self.english is not None :
            self.english  = None

class EduManagement :
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = []


#添加学生成绩
    def addStudent(self): 
        name = input("请输入学生姓名")
        #判断学生姓名
        for s in self.student_list :
            if s.name == name:
                print("该学生已经存在，添加失败")
                return
        chinese = int(input("请输入学生语文成绩"))
        math = int(input("请输入学生数学成绩"))
        english = int(input("请输入学生英语成绩"))
        #判断分数是否合法
        if  0<= chinese <=100 and 0  <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("学生的成绩必须得在0到100之间")
            
#修改学生成绩
    def change_score(self) :
        name = input("请输入学生姓名")
        for s in self.student_list :
            if name not in s.name :
                print("该学生未添加")
                return
        chinese = int(input("请输入语文成绩"))
        math  = int(input("请输入数学成绩"))
        english  = int(input("请输入英语成绩"))
        if  0<= chinese <=100 and 0  <= math <= 100 and 0 <= english <= 100:
            self.student_list[name].chinese = chinese
            self.student_list[name].math = math
            self.student_list[name].english = english
        else:
            print("成绩应该在0到100之间")
#删除学生成绩
    def remove_score(self):
        name = input("请输入学生姓名")
        for s in self.student_list :
            if name not in s.name :
                    print("该学生未添加")
                    return
        self.student_list[name].chinese = 0
        self.student_list[name].math = 0
        self.student_list[name].english = 0
#查询指定学生成绩
    def show_score(self):
        name = input("请输入学生姓名")
        for s in self.student_list :
            if name not in s.name :
                    print("该学生未添加")
                    return
            else:
                print(f"语文成绩为{s.chinese}")
                print(f"数学成绩为{s.math}")
                print(f"英语成绩为{s.english}")       
#展示全部学生成绩
    def show_all_score(self):
        for s in self.student_list :
            print(f"该学生姓名为{s.name}")
            print(f"语文成绩为{s.chinese}")
            print(f"语文成绩为{s.chinese}")
            print(f"英语成绩为{s.english}")   