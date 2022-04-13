a=int(input())
b=list(map(int,input().split(" ")))

c=0
d=0
for i in b:
    c=c+i
    k=abs(i-(c//a))
    d=k+d

print(d//2)


