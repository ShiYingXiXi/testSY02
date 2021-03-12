import requests
# HTTPBasicAuth 鉴权 鉴权就是有些动作必须登录之后才有权限操作，如Jenkins必须登录后才能构建项目，Jenkins用的鉴权方式是basic_auth,具体使用
# 方法如下
from requests.auth import HTTPBasicAuth
requests.post(url,data={},auth=('用户名','密码'))