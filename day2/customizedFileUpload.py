# -*- coding:utf-8 -*-
import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
#自定义文件名，文件类型、请求头
files = {
        'file':('test.png',open('test.png','rb'),'image/png')
}

r = requests.post(url,files=files)
# print (r.text)heman793