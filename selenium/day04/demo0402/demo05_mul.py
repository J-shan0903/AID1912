from day04.day0401.calculator import Count
import unittest
class TestMul(unittest.TestCase):
    def setUp(self):
        print("测试mul函数开始")

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

    def tearDown(self):
        print("测试mul结束")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    case_mul1 = TestMul("test_mul1")
    case_mul2 = TestMul("test_mul2")
    suite.addTest(case_mul1)
    suite.addTest(case_mul2)
    runner = unittest.TextTestRunner()
    runner.run(suite)