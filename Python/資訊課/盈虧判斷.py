k=[]
n=int(input())
for i in range (1,n):
    if n%i == 0:
        k.append(i)
    if sum(k)>n:
        print("盈數")
    elif sum(k)<n:
        print("虧數")
    elif sum(k)==n:
        print("完全數")