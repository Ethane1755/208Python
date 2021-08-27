
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)
    
m = int(input("Please input the first number here："))
n = int(input("Please input the second number here："))

if gcd(m,n) == 1:
    print('最大公因數:兩數互質')
else:
    print('最大公因數:',gcd(m,n))
print("最小公倍數:",lcm(m, n))
