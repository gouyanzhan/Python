import urllib,urllib3  # 导入这两个模块
import requests

count = 1000000
if count <= 2000000:
    while True:
        count +=1
        try:
            url = 'https://api.douban.com/v2/book/%s' %count
            url2 = urllib3.Request(url)
            response = urllib3.urlopen(url2)
            apicon = response.read()
            print (apicon)
        except urllib3.HTTPError:
            print("error,urllib3.HTTPError : %s" %count)
