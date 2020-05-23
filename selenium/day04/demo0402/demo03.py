from day04.demo0402.student import Student
import unittest
class TestStudent(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    def test_display1(self):
        Tom = Student("Tom",14,"五年级")
        Tom.display()
        self.assertIsInstance(Tom,Student)

    def test_display2(self):
        Jack = Student("Jack",10)
        Jack.display()
        self.assertIsInstance(Jack,Student)

    def tearDown(self) :
        print("测试结束\n_____________")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    case1 = TestStudent("test_display1")
    case2 = TestStudent("test_display2")
    suite.addTest(case1)
    suite.addTest(case2)

    runner = unittest.TextTestRunner()
    runner.run(suite)
