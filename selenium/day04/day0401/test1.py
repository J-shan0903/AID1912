from calculator import Count

class TestCount:
    def tast_add(self):
        c1 = Count(10,20)
        res1 = c1.add()
        if res1 ==30:
            print("计算正确！")
        else:
            print("计算错误！")
        print("计算实际结果：",res1)

mytest = TestCount()
mytest.tast_add()