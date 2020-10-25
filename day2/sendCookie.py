#发送cookie到服务器
import requests
import json

host = "http://httpbin.org"
endpoint = "cookies"

url = ''.json([host,endpoint])
#法一：简单发送
cookies = {"aaa":"bbb"}
r = requests.get(url,cookies=cookies)
print(r.text)

#法二：复杂发送
s = requests.session()
c = requests.cookies.RequestsCookieJar()
c.set('c-name','c-value',path='/xxx/uuu',domain = '.test.com')
s.cookies.update(c)