# -*- coding:utf-8 -*-
#带参数的get

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
payload = {"show_env":"1"}
r = requests.get(url=url,params=payload)

print (r.url)