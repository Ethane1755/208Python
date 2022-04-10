c=input()
k=[]
k.append(c.split())

l=len(k)
m=0
n=0
for i in range (1,l+1):
    d=k[m]
    m=m+1
    l=len(d)
    for j in range (1,l+1):
        print(d[n])
        n=n+1
        