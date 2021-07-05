# Author:   jingnan
# Date:    2021/7/6
# Desc:   封装get post请求
import requests


login_url = 'http://localhost:8089/user/login.do'
login_data = {'username': 'admin', 'password': 'admin'}
get_category_url = 'http://localhost:8089/manage/category/get_category.do?categoryId=100001'

login_res = requests.post(login_url, login_data)
print(login_res.status_code)
print(login_res.text)
print(login_res.json())
print(login_res.cookies)
# header必须是字典格式
print(login_res.request.headers)

get_category_res = requests.get(get_category_url, cookies=login_res.cookies)
print(get_category_res.json())

# 创建一个会话
session = requests.session()
# 在会话中进行登陆
login_res = session.post(login_url, params=login_data)
# 在会话中执行其他需要登陆的接口，可以不用在传递cookie，因为在这个会话中已经执行过登陆接口
get_category_res_2 = session.get(get_category_url)
print(get_category_res_2.json())




