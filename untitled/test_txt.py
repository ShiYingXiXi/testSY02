import unittest
from ddt import ddt,data,unpack
def read_txt():
    list = []
    file = open('/Users/shiying/test.txt','r',encoding='utf-8')
    for line in file.readlines():
        list.append(line.strip('\n').split())
    return list

@ddt
class aaa(unittest.TestCase):
    def setUp(self):
        pass
    @data(*read_txt())
    def test1_data(self,args1):
        print(args1)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()


