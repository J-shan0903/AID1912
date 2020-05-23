from day04.demo0402.demo05_div import TestDiv
from day04.demo0402.demo05_mul import TestMul
from day04.demo0402.demo04 import TestSub,TestAdd
import unittest
if __name__ == '__main__':
    suite = unittest.TestSuite()
    case1 = TestAdd("test_add1")
    suite.addTest(case1)
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestAdd("test_add3"))

    case_sub1 = TestSub("test_sub1")
    suite.addTest(case_sub1)
    case_sub2 = TestSub("test_sub2")
    suite.addTest(case_sub2)

    case_mul1 = TestMul("test_mul1")
    case_mul2 = TestMul("test_mul2")
    suite.addTest(case_mul1)
    suite.addTest(case_mul2)

    case_div1 = TestDiv("test_div1")
    case_div2 = TestDiv("test_div2")
    suite.addTest(case_div1)
    suite.addTest(case_div2)
    runner = unittest.TextTestRunner()
    runner.run(suite)