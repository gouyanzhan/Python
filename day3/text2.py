import requests

url ="https://boss-stage.yit.com/apigw/m.api"

headers = {
    "user-agent":"yit.tester",
    "referer":"https://boss-stage.yit.com/login.html?v=1601373599713"
    "user-agent"
}
payload = {"username":"jessica","password":"Yit123","_mt":"sam.loginInBoss"}

response = requests.post(url,headers=headers,data=payload)

print(response.text)
print(response.status_code)