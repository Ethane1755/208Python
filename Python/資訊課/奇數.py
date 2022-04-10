a=input()
c=input()
k=[]
k.append(c.split())

l=len(k)
m=0

for i in range (1,l+1):
    d=k[m]
    m=m+1

n=0
g=0
h=0
for i in d:
    d[n]=int(d[n])
    if d[n]%2==0:
        g=g+d[n]
    else:
        h=h+d[n]
    n=n+1
print(g,h)