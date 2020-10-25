def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return number * 3 + 1
while True:
    try:
        n = int(input('请输入一个大于零的整数，按enter键确定'))
        if n <= 0:
            print('输入错误，请输入一个大于零的整数，按enter键确定，重新输入')
            continue
        break
    except:
        print('请输入整数')
x = collatz(n)
print(x)
while True:
    if x == 1:
        break
    x = collatz(x)
    print(x)