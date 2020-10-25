import requests
import json
host = "http://httpbin.org"
endpoint = "headers"

url = ''.join([host,endpoint])
header1 = {'testA':'AAA'}
header2 = {'testB':'BBB'}

s = requests.session()
s.headers.update(header1)
r = s.get(url,headers = header2)

print(r.text)

print("-----------")

s.headers['testA'] = None     #删除会话里的信息testA
r1 = s.get(url,headers = header2)
print(r1.text)

