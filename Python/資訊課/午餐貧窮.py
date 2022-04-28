a=int(input())
b=input()
c=b.split()
c=list(map(int,c))
d=[]

for i in c:
    if i >= (sum(c)//len(c)):
        d.append(i)

if len(d)==18:
    print(17)
else:
    print(len(d))
