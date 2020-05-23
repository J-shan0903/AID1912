import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

