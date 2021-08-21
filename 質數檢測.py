def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = int(input('輸入一個正整數:'))

if n ==1:
    print('不是質數')
elif is_prime(n):
    print('是質數')
else:
    print('不是質數')

