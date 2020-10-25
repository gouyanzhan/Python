def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    else:
        number = 3 *number + 1
        return number
print('Ennter number:')
typeNumber = int(input())
while typeNumber != 1:
    print(collatz(typeNumber))
    typeNumber = collatz(typeNumber)
    if typeNumber == 1:
        print(typeNumber)
        break


