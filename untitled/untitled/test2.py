import requests
import json
from _ast import Try
from django.template.context_processors import request


class send():
    #1.get方式，无参数访问接口

    def send_get(self, url, data, headers=None):
        res = requests.get(url, params=data, headers=headers)
        return res
    #2.post方式，url格式入参访问接口
    def send_post_url(self,url,data,headers = None):
        res = requests.post(url, params=data, headers=headers)
        return res
    #3.post方式，form-data格式访问接口
    def send_post_fdata(self, url, data, headers=None):
        res = requests.post(url,params=data, headers=headers)
        return res
    #4.post方式，json格式访问接口 公司一般是传的json文件 即
    def send_post_jsonData(self, url, data, headers = {'content-type': 'application/json'}):
        #当文件头是json时，发送post请求参数data=值，值必须是json(字符型)
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        res = requests.post(url, data=json_data, headers=headers)
        return res
    def cookies(self,url):
        res = requests.get(url)
        #保存cookieJar对象：
        cookieJar = res.cookies
        cookiedict = requests.utils.dict_from_cookiejar(cookieJar)
        return cookiedict
    def session(self):
        # 1. 创建session对象
        ssion = requests.session()
        # 2. 设置headers
        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
        #            "Accept": "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
        #            "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.5"}

        headers = {'Server': 'Apache/2.2.15 (CentOS)', 'X-Powered-By': 'PHP/5.6.30', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE,x-requested-with,Authorization,token', 'Access-Control-Allow-Credentials': 'true', 'Content-Length': '94', 'Connection': 'close', 'Content-Type': 'text/html; charset=utf-8'}

        # 3. 设置登录入参
        data = {"name": "超级管理员", "password": "1198a27c0ce9c9556f4cea38f905f5ae"}
        # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存至sesion
        ssion.post("http://h5.c-lap.cn/oa_api/public/index/oa/login", data=data, headers=headers)
        # 5. 直接访问需要登录的页面
        # res = ssion.post(url,)
        res = ssion.get('http://h5.c-lap.cn/oa_api/public/index/activity/offline_activity')
        return res

    SessionRequest = requests.session()


    def ssl(self):
        # https协议默认verify = True需要证书验证，verify = False表示不验证证书
        res = requests.get("https://www.12306.cn/index/", verify=False)
        return res

if __name__ == "__main__":
     # 1.get方式，无参数访问接口
     res1 = send().send_get('http://120.27.198.185/thinkphp5/public/index/page/eleven_page', {})
     print('1.get方式，无参数访问接口,返回值：')
     # 响应内容json格式转字典
     print(res1.json())
     print('-------开始打印request常见响应方法内容---------------')
     print('查看响应内容，res.text 返回的是Unicode格式的数据')
     print(res1.text)
     print('查看响应内容，res.content返回的字节流数据(主要用于存储图片)')
     print(res1.content)
     print('查看完整url地址，res.url')
     print(res1.url)
     print('查看响应头部字符编码，res.encoding')
     print(res1.encoding)
     print('查看响应码，res.status_code')
     print(res1.status_code)
     print('-------结束打印request常见响应方法内容---------------')


     # # 2.post方式，url格式入参访问接口
     # res2 = send().send_post_url('http://120.27.198.185/oa_api/public/index/product/package_list',
     #                             {"product_name": "", "limit": "10", "page": "1", "status": ""})
     # print('2.post方式，url格式入参访问接口,返回值：')
     # print(res2.json())
     # # 3.post方式，form-data格式入参访问接口
     res3 = send().send_post_jsonData('http://120.27.198.185/thinkphp5/public/index/page/yichuan_climb', {"mobile":"40000004003","kid_name":"宝宝姓名",
"birth_date":"2018-10-10",
"code":"1234",
"real_name":"家长姓名"
})
     print('3.post方式，form-data格式入参访问接口,返回值：')
     print(res3.json())
     # # 4.post方式，josn格式入参访问接口

     res4 = send().send_post_jsonData('http://120.27.198.185/oa_api/public/index/oa/login', {"name": "超级管理员", "password": "1198a27c0ce9c9556f4cea38f905f5ae"})
     print('4.post方式，josn格式入参访问接口,返回值：')
     print(res4.json())
     print(res4.cookies)

     res5 = send().cookies('http://www.baidu.com')
     print('5.访问百度打印colies,返回值：')
     print(res5)

     res6 = send().session()
     print('6.需要登录才可以看到资源，通过session可直接查看,返响应状态码：')
     print(res6.status_code)
     # print(res6.cookies)
     # print(res6.headers)
     print(res6.json())


     # res7 = send().ssl()
     # print('7.访问12306,设置不验证ssl,verify = False，返响应状态码：')
     # print(res7.status_code)


