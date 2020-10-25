# 将python数据转化为json数据
import json
data = {'id':1,'name':'51zxw','password':'666666'}
print(type(data))
json_str = json.dumps(data)
print(type(json_str))
print(json_str)