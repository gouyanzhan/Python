import requests

url = "https://boss-stage.yit.com/apigw/m.api"

# payload = '_mt=lotteryBoss.createOrUpdateLotteryReceiveWay&lotteryReceiveWayRequest=%7B%22lotteryActivityId%22%3A30%2C%22freeCode%22%3Atrue%2C%22freeCodeTimes%22%3A1%2C%22taskReceiveWayConfigRequestList%22%3A%5B%7B%22receiveCodeWayType%22%3A%22TASK%22%2C%22referenceTaskId%22%3A1798%7D%2C%7B%22receiveCodeWayType%22%3A%22TASK%22%2C%22referenceTaskId%22%3A1799%7D%5D%7D'
headers = {
  'user-agent': 'yit.tester',
  'content-type': 'application/x-www-form-urlencoded',
  '_tk': 'Bearer utk_mDIDhhPIg99Pw4b8bJ8rwXnnjRNpEjL9BqualzgvnB7VCpo6Y7oUinj5VRGZApwGlhUXTGEkIPMBO/wTsr/1PpIG9LCOXgP5vlt13x2w2eSbL6YPUtaRXS/Lhb+nr0Ms3pVa8xR6Mw3rp+QD0/Ev5w==',
  'Cookie': '__did=-888526642799650; 0__operator=%E7%BC%91%E5%BB%B6%E5%B1%95; 0__ct=1; 0__tk=utk_bLpNhNM95mTeqhQ8uGRPMiXtTyEKWn0Ghd5wQVXwcqu7caxbnoJf9mlgKaky3MeyOKOoOg2b%2BcCnE%2FRACk7dZX97PBqEUnVrSjdw5TRJr09f2nBDrydCvbx9AJc2OK2kXVCKSFq9yIR2bjiZunOHZw%3D%3D'
}
payload = {'_mt':'lotteryBoss.createOrUpdateLotteryReceiveWay','lotteryReceiveWayRequest':'{"lotteryActivityId":36,"freeCode":true,"freeCodeTimes":1,"taskReceiveWayConfigRequestList":[{"receiveCodeWayType":"TASK","referenceTaskId":2256}]}'}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
