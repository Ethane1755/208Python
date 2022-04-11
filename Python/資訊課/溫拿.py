a=int(input())
c=input()
k=[]
k.append(c.split())

l=len(k)
m=0

for i in range (1,l+1):
    d=k[m]
    m=m+1
    l=len(d)

asd=[int(element)for element in d]
j=min(asd)
e=max(asd)

b=[]
z=[]

for i in asd:
    if i==j:
        b.append(i)
    elif i==e:
        z.append(i)

print(asd.index(z[0])+1,asd.index(b[0])+1)