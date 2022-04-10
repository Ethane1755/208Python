a=int(input())
b=int(input())

for i in range (a,b+1):
    if i%7==0 or i%10==7:
        print(i, end=' ')