from day04.day0401.calculator import Count
from day04.demo0402.demo06 import MyTest

# 测试sub函数
class TestSub(MyTest):
    def test_sub1(self):
        print("测试整数sub")
        m1 = Count(100,20)
        res1 = m1.sub()
        print("实际计算结果",res1)
        self.assertEqual(res1,80)
    def test_sub2(self):
        print("测试浮点数sub")
        m2 = Count(4589.87,3978.78)
        res2 = m2.sub()
        print("实际计算结果：",res2)
        if abs(res2-611.09)<0.01:
            res2 = 611.09
        self.assertEqual(res2, 611.09)