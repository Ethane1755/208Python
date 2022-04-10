a=input()
c=input()
k=[]
k.append(c.split())

l=len(k)
m=0

for i in range (1,l+1):
    d=k[m]
    m=m+1

print(d.index(max(d))+1,d.index(min(d))+1)
