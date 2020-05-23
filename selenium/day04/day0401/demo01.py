#步骤1：导入unittest模块
import unittest
from day04.day0401.calculator import Count

# 步骤2：编写测试类TestCount ，继承TestCase 类
class TestCount(unittest.TestCase):
    # 步骤3：重写sutUp函数
    def setUp(self):
        print("测试开始")

    def test_add1(self):
        print("测试两个整数函数")
        c1 = Count(10,20)
        res1 = c1.add()
        print("计算实际结果：",res1)
    # 步骤5：使用unittest 提供的断言函数
        self.assertEqual(res1,30)

    # 步骤6:编写tearDown函数
    def tearDown(self):
        print("测试结束")

# 步骤7：调用unittest提供的main()函数，执行测试用例
if __name__ == '__main__':
    unittest.main()
