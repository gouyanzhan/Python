#获取cookie
import requests
import json

url = "https://www.baidu.com"
r = requests.get(url)

#将requesCookieJar转换成字典
c = requests.utils.dict_from_cookiejar(r.cookies)

print (r.cookies)
print(c)

for a in r.cookies:
    print (a.name,a.value)