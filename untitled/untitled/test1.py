import json
import requests


class jsonC():
    def __init__(self):
        self.url = 'http://wthrcdn.etouch.cn/weather_mini?city=北京'
        self.geturl = requests.get(self.url)


    # 字典转json,因为python没json类型所以str表示
    def dict_json(self):
        d = {"name": "张三", "age": 18}
        j = json.dumps(d, ensure_ascii=False)
        print('dict_json函数：类型：', type(d), '转类型', type(j), '\n', j)

    # json转字典
    def json_dict(self):
        s = '{"name":"张三","age":18}'
        d = json.loads(s)
        print('json_dict函数：类型：', type(s), '转类型', type(d), '\n', d)

    # 接口调用直接返回 字典（dict）
    def get_json(self):
        d = self.geturl.json()
        print('get_json函数类型：', type(d), '\n', d)

    # 接口调用直接返回字符串
    def get_str(self):
        s = self.geturl.text
        print('get_str函数返回类型：', type(s), '\n', s)


if __name__ == "__main__":
    js = jsonC()
    js.dict_json()
    js.json_dict()
    js.get_json()
    js.get_str()
