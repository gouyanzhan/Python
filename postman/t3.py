import requests

url = "https://boss-stage.yit.com/apigw/m.api"

payload = '_mt=taskBoss.createTaskByTemplate&createTaskByTemplateReq=%7B%22referenceId%22%3A30%2C%22taskTemplateId%22%3A1%2C%22completeLimitNum%22%3A1%2C%22awardType%22%3A%22LOTTERY_CODE%22%2C%22awardAmount%22%3A1%2C%22autoIssue%22%3Atrue%2C%22taskTitle%22%3A%22%u5173%u6CE8%u5E97%u94FA%22%2C%22receiveType%22%3A%22MANUAL_RECEIVE%22%2C%22activeTime%22%3A%222020-09-23%2017%3A44%3A33%22%2C%22inactiveTime%22%3A%222020-09-24%2017%3A44%3A33%22%2C%22templateParamList%22%3A%5B%7B%22desc%22%3A%22%u5E97%u94FA%20id%22%2C%22key%22%3A%22id%22%2C%22value%22%3A%223%22%7D%5D%7D'
headers = {
  'user-agent': 'yit.tester',
  'content-type': 'application/x-www-form-urlencoded',
  '_tk': 'Bearer utk_mDIDhhPIg99Pw4b8bJ8rwXnnjRNpEjL9BqualzgvnB7VCpo6Y7oUinj5VRGZApwGlhUXTGEkIPMBO/wTsr/1PpIG9LCOXgP5vlt13x2w2eSbL6YPUtaRXS/Lhb+nr0Ms3pVa8xR6Mw3rp+QD0/Ev5w==',
  'Cookie': '__did=-888526642799650; 0__operator=%E7%BC%91%E5%BB%B6%E5%B1%95; 0__ct=1; 0__tk=utk_bLpNhNM95mTeqhQ8uGRPMiXtTyEKWn0Ghd5wQVXwcqu7caxbnoJf9mlgKaky3MeyOKOoOg2b%2BcCnE%2FRACk7dZX97PBqEUnVrSjdw5TRJr09f2nBDrydCvbx9AJc2OK2kXVCKSFq9yIR2bjiZunOHZw%3D%3D'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
