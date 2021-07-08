# Author:   jingnan
# Date:    2021/7/6
# Desc: 执行入口
from utils.http_util import HttpRequest


def run():
    httpRequest = HttpRequest()

    login_url = 'http://localhost:8089/user/login.do'
    login_data = {'username': 'admin', 'password': 'admin'}
    get_category_url = 'http://localhost:8089/manage/category/get_category.do?categoryId=100001'

    login_res = httpRequest.service(login_url, 'post', login_data)
    print(login_res.status_code)
    print(login_res.json())

    get_category_res = httpRequest.service(get_category_url, 'get', cookies=login_res.cookies)
    print(get_category_res.json())


run()

