class Student:
    def __init__(self,name,age,grade="一年级"):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("姓名：",self.name)
        print("年龄：",self.age)
        print("年级：",self.grade)

if __name__ == '__main__':
    xiaoming = Student("小名",12,"三年级")
    xiaoming.display()
    xiaogang = Student("小刚",13,"四年级")
    xiaogang.display()
