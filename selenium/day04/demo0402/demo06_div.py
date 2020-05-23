from day04.day0401.calculator import Count
from day04.demo0402.demo06 import MyTest
class TestDiv(MyTest):
    def test_div1(self):
        print("测试两个整数div")
        c1 = Count(100,20)
        res1 = c1.div()
        print("实际计算结果：",res1)
        self.assertEqual(res1,5)

    def test_div2(self):
        print("测试两个浮点型数据div")
        c2 = Count(245.45,34.67)
        res2 = c2.div()
        print("实际计算结果：",res2)
        if abs(res2-7.0796)<0.01:

            res2 = 7.0796
        self.assertEqual(res2,7.0796)