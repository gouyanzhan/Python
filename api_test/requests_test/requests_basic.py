import requests

base_url = 'http://httpbin.org'

r = requests.get(base_url + '/get')
print(r.status_code)

r = requests.post(base_url + '/post')
print(r.status_code)

r = requests.put(base_url + '/put')
print(r.status_code)

r = requests.delete(base_url + '/delete')
print(r.status_code)

#参数传递
param_data = {'user':'zxw','password':'666666'}
r = requests.get(base_url + '/get',param_data)
print(r.url)
print(r.status_code)

from_data = {'user':'51zxw','password':'8888'}
r = requests.post(base_url + '/post',from_data)
print(r.text)

#请求头定制
from_data = {'user':'51zxw','password':'8888'}
header = {'user-agent':'Mozill/5.0'}
r = requests.post(base_url + '/post',data=from_data,headers = header)
print(r.text)

#cookie 设置
cookie = {'user':'51zxw'}
r = requests.get(base_url+'/cookies',cookies = cookie)

r = requests.get('http://www.baidu.com')
print(r.cookies)
print(type(r.cookies))
for key,value in r.cookies.items():
    print(key + ':' + value)