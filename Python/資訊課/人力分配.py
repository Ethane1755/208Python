a=input()
a1,b1,c1=a.split()
a1=int(a1)
b1=int(b1)
c1=int(c1)
b=input()
a2,b2,c2=b.split()
a2=int(a2)
b2=int(b2)
c2=int(c2)
c=int(input())

l=[]
for X1 in range(c+1):
    Y1 = a1*X1*X1+b1*X1+c1
    Y2 = a2*(c-X1)*(c-X1)+b2*(c-X1)+c2
    k=Y1+Y2
    l.append(k)
print(max(l))