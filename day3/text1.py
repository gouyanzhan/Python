import requests

class HttpRequest:
    """
    封装http请求，get post等，必要参数：
    method，请求方式；url，请求地址；cookie,cookie;data，需要发送的正文数据；
    动态参数 **kwargs，如headers json等；
    调用时赋值即可，如 headers=a，json=b
    """
    def request(self,method,url,cookie=None,data=None,**kwargs):
        try:
            response = requests.request(method,url,cookies=cookie,data=data,**kwargs)
        except Exception as e:
            print("请求报错：{}".format(e))
            raise e
        return response