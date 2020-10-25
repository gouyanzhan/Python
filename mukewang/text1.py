# 排序
alist = [0,10,88,19,9,1]
print(sorted(alist))   #从小到大，不改变原有列表
print(sorted(alist,reverse=True))  #从大到小，不改变原有列表
print(alist)

alist.sort()      # 改变原有列表
print(alist)

alist.sort(reverse=True)    # 改变原有列表
print(alist)
