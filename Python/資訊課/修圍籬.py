a=int(input())
b=input()
c=b.split()
c=list(map(int,c))
d=[]

for i in c:
    if i==0:
        if c.index(i)==0:
            d.append(c[1])
        elif c.index(i)==a-1:
            d.append(c[-2])
        else:
            if c[c.index(i)-1]>c[c.index(i)+1]:
                d.append(c[c.index(i)+1])
            elif c[c.index(i)-1]<c[c.index(i)+1]:
                d.append(c[c.index(i)-1])
            else:
                d.append(c[c.index(i)-1])
        p=c.index(i)
        c[p]=100
print(sum(d))

