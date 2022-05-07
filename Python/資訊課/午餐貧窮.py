a=int(input())
b=input()
c=b.split()
c=list(map(int,c))
d=[]

for i in c:
    if i >= (sum(c)//len(c)):
        d.append(i)


print(len(d))
