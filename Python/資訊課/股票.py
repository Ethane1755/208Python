a=input()
b,c=a.split()
b=int(b)
c=int(c)
d=input()
d=d.split()
d=list(map(int,d))
k=d[0]
l1=[]
m=1
d.remove(d[0])
for i in d:
    if i >=k+c and m==1:
        l1.append(i)
        m=0
    if m==0 and i<=k-c:
        l1.append(-i)
        m=1
    print(i,m)
print(l1)
print(int(sum(l1)))
