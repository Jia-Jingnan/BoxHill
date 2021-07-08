# Author:   jingnan
# Date:    2021/7/6
# Desc:   封装get post请求
import requests


class HttpRequest:

    def service(self, url, method, data=None, cookies=None):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, data, cookies=cookies)

            elif method.upper() == 'POST':
                response = requests.post(url, data, cookies=cookies)

            else:
                print('Bad Request！')
        except Exception as e:
            print('Bad Request:{}'.format(e))
            raise e

        return response


if __name__ == '__main__':

    httpRequest = HttpRequest()

    login_url = 'http://localhost:8089/user/login.do'
    login_data = {'username': 'admin', 'password': 'admin'}
    get_category_url = 'http://localhost:8089/manage/category/get_category.do?categoryId=100001'

    login_res = httpRequest.service(login_url, 'post', login_data)
    print(login_res.status_code)
    print(login_res.json())

    get_category_res = httpRequest.service(get_category_url, 'get', cookies=login_res.cookies)
    print(get_category_res.json())

    # # 创建一个会话
    # session = requests.session()
    # # 在会话中进行登陆
    # login_res = session.post(login_url, params=login_data)
    # # 在会话中执行其他需要登陆的接口，可以不用在传递cookie，因为在这个会话中已经执行过登陆接口
    # get_category_res_2 = session.get(get_category_url)
    # print(get_category_res_2.json())




