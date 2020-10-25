# -*- coding:utf-8 -*-
import requests
import json

host = "http://httpbin.org/"
endpoint = "post"
url = ''.join([host,endpoint])
payload = {'key1':'value1','key2':'value2'}

r = requests.post(url,data=payload)
#response = r.json()
print (r.text)