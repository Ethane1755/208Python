n=int(input())
d=int(input())
a=list(input().split())
a=list(map(int,a))

def buy(m,x):
    if m<=x-d:
        b=balance-m
        s=1
        balance=b

def sell(m,x):
    if m>=x+d:
        b=balance+m
        s=0
        balance=b

balance=-a[0]
s=1
a.remove(a[0])

for i in a:
    if s==0:
        buy(i,abs(balance))
    if s==1:
        sell(i,abs(balance))

print(balance)
