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
        if english is not None :
            self.english  = english

class EduManagement :
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = []

#添加学生成绩
    def add_Student(self): 
        name = input("请输入学生姓名:")
        #判断学生姓名
        for s in self.student_list :
            if s.name == name:
                print("该学生已经存在，添加失败")
                return
        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))
        #判断分数是否合法
        if  0<= chinese <=100 and 0  <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("学生的成绩必须得在0到100之间")
            
#修改学生成绩
    def update_student(self) :
        name = input("请输入要修改的学生姓名:")
        for s in self.student_list :
            if name == s.name :
                print(f"当前成绩:{s}")
                chinese = int(input("请输入修改后的语文成绩:"))
                math  = int(input("请输入修改后的数学成绩:"))
                english  = int(input("请输入修改后的英语成绩:"))
                if  0<= chinese <=100 and 0  <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("成绩应该在0到100之间")
                    return
        print("未找到该学生，修改失败")
        
        
#删除学生成绩
    def delete_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list :
            if name == s.name :
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败")
        
#查询指定学生成绩
    def show_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list :
            if name == s.name :
                print(f"该学生的成绩为:{s}")
                return
        print("未找到该学生")
                  
#展示全部学生成绩
    def show_all_student(self):
        for s in self.student_list :
           print(s)
    def run(self):
        print(f"欢迎使用学生管理系统{EduManagement.system_version}")
        while True:
            print()
            print("##########################################################################")
            print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 #")
            print("##########################################################################")
            print()

            choice = input("请输入要执行的操作,输入1-6:")
            match choice :
                case "1":
                    self.add_Student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.show_student()
                case "5":
                    self.show_all_student()
                case "6":#退出while用break,退出for 中的if用return
                    print("拜拜")
                    break 
                case _:
                    print("请输入有效操作")


if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()