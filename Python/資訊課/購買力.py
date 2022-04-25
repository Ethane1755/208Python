a=input()
b,c=a.split()
b=int(b)
c=int(c)
l1=[]
l2=[]


for i in range(b):
    k=input()
    h=k.split()
    h=list(map(int,h))
    for j in h:
        if (max(h)-min(h))>=c:
            l1.append(j)
            l2.append(1)

print(int(len(l2)/len(h)),int(sum(l1)/len(h)))
    