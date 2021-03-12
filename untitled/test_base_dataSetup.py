#ddt 常用模块
# @ddt(申明当前类使用ddt框架)
# @data(用于传参)
# @unpack(将参数解包，一般针对元组和列表)
# @data_file(ddt读取yaml/json文件)
import unittest
from ddt import ddt, data, unpack
@ddt()
class FooTest(unittest.TestCase):
    @data(100)
    def testCase1(self, name):
        print(name)
    @data('诸葛')
    def testCase2(self, name):
        print(name)

    @data(('诸葛', '司马'))
    @unpack
    def test1_data(self, args1, args2):
        print(args1, args2)

    @data(['诸葛', '司马'])
    @unpack
    def test2_data(self, args1, args2):
        print(args1, args2)

if __name__ == '__main__':
    unittest.main()


