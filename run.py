# Author:   jingnan
# Date:    2021/7/6
# Desc: 执行入口
from utils.http_util import HttpRequest

# 登陆接口测试用例
# cases = [
#     {'http://localhost:8089/user/login.do', 'post', {'usename': 'admin', 'password': 'admin'}, '0'},
#     {'http://localhost:8089/user/login.do', 'post', {'usename': 'admin1', 'password': 'admin'}, '1'},
#     {'http://localhost:8089/user/login.do', 'post', {'usename': 'admin', 'password': 'admin1'}, '1'}
# ]



def run(cases): # 传列表嵌套字典的测试用例

    for item in cases:
        print('开始执行:',item['desc'])
        res =  HttpRequest().service(item['login_url'], item['method'], item['login_data'])
        print('响应报文:', res.json())


cases = [
    {'login_url': 'http://localhost:8089/user/login.do', 'method': 'post', 'login_data': {"username": "admin", "password": "admin"}, 'desc': '正常登陆'},
    {'login_url': 'http://localhost:8089/user/login.do', 'method': 'post', 'login_data': {"username": "admin1", "password": "admin"}, 'desc': '异常登陆'}
]

run(cases)

