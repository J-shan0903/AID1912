import unittest
from day04.day0401.calculator import Count
from day04.demo0402.demo06 import MyTest

# 步骤2：编写测试类TestCount ，继承TestCase 类
class TestAdd(MyTest):
    def test_add1(self):
        print("测试两个整数函数")
        c1 = Count(10,20)
        res1 = c1.add()
        print("计算实际结果：",res1)
    # 步骤5：使用unittest 提供的断言函数
        self.assertEqual(res1,30)

    def test_add2(self):
        print("测试两个浮点型数据函数")
        c2=Count(2167.45,3978.78)
        res2=c2.add()
        print("计算实际结果：",res2)
        if abs(res2-6146.23)<0.001:
            res2 = 6146.23
        self.assertEqual(res2,6146.23)

    def test_add3(self):
        print("测试两个字符串函数")
        c3 = Count("你好","测试")
        res3 =c3.add()
        print("实际计算结果：",res3)
        self.assertEqual(res3,"你好测试")


