import json
import requests
class RunMain:

    def __init__(self,url,method,data = None):         #构造方法
       self.res = self.run_main(url,method,data )
    def send_get(self,url,data):        #每一个类里面都要加一个self
        res = requests.get(url = url,data = data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def send_post(self,url,data):
        res = requests.post(url = url,data = data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':

    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
    'cart'
}
    run = RunMain(url,'GET',data)
    print(run.res)
