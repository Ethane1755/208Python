a=int(input())
b=input()
c=b.split()
c=list(map(int,c))
d=[]

for i in c:
    if i>=60:
        d.append(i)
e=min(d)
f=c.index(e)+1
d.sort()
print(f,d[0])