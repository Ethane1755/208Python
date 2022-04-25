k=input()
a,b=k.split()
a=int(a)
b=int(b)
c=int(input())
l=[]
for i in range(c):
    l1=[]
    l2=[]
    m=input()
    n=m.split()
    n=list(map(int,n))
    for j in n:
        if abs(j)==a:
            l1.append(j)
        elif abs(j)==b:
            l2.append(j)
    if sum(l1)>0 and sum(l2)>0:
        l.append(1)

print(len(l))