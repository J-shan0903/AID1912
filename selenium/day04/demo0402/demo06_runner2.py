import unittest
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='demo06*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
