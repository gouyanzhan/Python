#素数
#0，1不是素数
#除了1和它自身外，不能被其他自然数整除的数

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True
for i in range(0,100):
    if is_prime(i):
        print (i)
