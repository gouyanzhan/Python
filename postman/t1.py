import requests

url = "https://boss-stage.yit.com/apigw/m.api"

# payload = '_mt=lotteryBoss.createOrUpdateLotteryActivity&lotteryCreateRequest=%7B%22lotteryActivityId%22%3A-1%2C%22activityName%22%3A%22jessica%u6D3B%u52A8%22%2C%22activityDesc%22%3A%22%u8FD9%u662F%u4E00%u4E2A%u6D3B%u52A8%u63CF%u8FF0%22%2C%22warmUpTime%22%3A%222020-09-18%2014%3A42%3A29%22%2C%22signUpStartTime%22%3A%222020-09-20%2014%3A42%3A29%22%2C%22signUpEndTime%22%3A%222020-09-21%2014%3A42%3A29%22%2C%22drawTime%22%3A%222020-09-22%2014%3A42%3A29%22%2C%22spreadType%22%3A%22ELECTRICITY%22%2C%22lotteryPrize%22%3A%7B%22prizeName%22%3A%22%u5956%u54C1%u540D%u79F0%22%2C%22prizeReferenceSpu%22%3A0%2C%22prizeAmount%22%3A1%2C%22price%22%3A20000%2C%22prizeMainImgUrl%22%3A%22https%3A//asset-i3.yit.com/LOTTERY/LOTTERY_ACTIVITY_CONFIG/6b44f1bb78d7bdf4423aee5ee84e08f9_640X480.jpeg%22%2C%22prizeThumbnailUrl%22%3A%22https%3A//asset-i3.yit.com/LOTTERY/LOTTERY_ACTIVITY_CONFIG/5f46ddc6f3ed59595a8751b02b08b9f5_640X640.jpeg%22%7D%7D'
headers = {
  'user-agent': 'yit.tester',
  'content-type': 'application/x-www-form-urlencoded',
  '_tk': 'Bearer utk_mDIDhhPIg99Pw4b8bJ8rwXnnjRNpEjL9BqualzgvnB7VCpo6Y7oUinj5VRGZApwGlhUXTGEkIPMBO/wTsr/1PpIG9LCOXgP5vlt13x2w2eSbL6YPUtaRXS/Lhb+nr0Ms3pVa8xR6Mw3rp+QD0/Ev5w==',
  'Cookie': '__did=-888526642799650; 0__operator=%E7%BC%91%E5%BB%B6%E5%B1%95; 0__ct=1; 0__tk=utk_bLpNhNM95mTeqhQ8uGRPMiXtTyEKWn0Ghd5wQVXwcqu7caxbnoJf9mlgKaky3MeyOKOoOg2b%2BcCnE%2FRACk7dZX97PBqEUnVrSjdw5TRJr09f2nBDrydCvbx9AJc2OK2kXVCKSFq9yIR2bjiZunOHZw%3D%3D'
}
payload = {'_mt':'lotteryBoss.createOrUpdateLotteryActivity',
           'lotteryCreateRequest':'{"lotteryActivityId":-1,"activityName":"jessica活动","activityDesc":"这是一个活动描述","warmUpTime":"2020-09-30 16:30:00","signUpStartTime":"2020-10-01 00:00:00","signUpEndTime":"2020-10-02 00:00:00","drawTime":"2020-10-03 00:00:00","spreadType":"ELECTRICITY","lotteryPrize":{"prizeName":"奖品名称","prizeReferenceSpu":0,"prizeAmount":1,"price":20000,"prizeMainImgUrl":"https://asset-i3.yit.com/LOTTERY/LOTTERY_ACTIVITY_CONFIG/6b44f1bb78d7bdf4423aee5ee84e08f9_640X480.jpeg","prizeThumbnailUrl":"https://asset-i3.yit.com/LOTTERY/LOTTERY_ACTIVITY_CONFIG/5f46ddc6f3ed59595a8751b02b08b9f5_640X640.jpeg"}}'}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
