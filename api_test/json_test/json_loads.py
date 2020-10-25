# 将json数据转化为python数据

import json

json_str = '{"id":1,"name":"51zxw","passw ord":"666666"}'
print(type(json_str))
data = json.loads(json_str)
print(type(data))
print(data)
print(data['id'])
print(data['name'])

# 写入
with open('data.json','w') as f:
    json.dump(data,f)

# 读取
with open('data.json','r') as f:
    data = json.load(f)
    print(data)

