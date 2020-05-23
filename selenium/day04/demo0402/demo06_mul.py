from day04.day0401.calculator import Count
from day04.demo0402.demo06 import MyTest

class TestMul(MyTest):
    def test_mul1(self):
        print("测试两个整数mul")
        c1 = Count(10,20)
        res1 = c1.mul()
        print("实际计算结果：",res1)
        self.assertEqual(res1,200)

    def test_mul2(self):
        print("测试两个浮点型数据mul")
        c2 = Count(20.45,45.67)
        res2 = c2.mul()
        print("实际计算结果：",res2)
        if abs(res2-933.9515)<0.01:

            res2 = 933.9515
        self.assertEqual(res2,933.9515)
