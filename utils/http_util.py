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





