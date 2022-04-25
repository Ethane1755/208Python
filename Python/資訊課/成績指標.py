a=int(input())
b=input()
c=b.split()
c=[int(x) for x in c]
c=sorted(c)
v=[str(x) for x in c]
print(" ".join(v))

d=[]
e=[]
f=[]
for i in c:
    if i < 60:
        d.append(i)
    elif i >=60:
        e.append(i)
    elif i==60:
        f.append(i)
d=sorted(d)
e=sorted(e)
if d!=[]:  
    print(d[-1])
elif f==[]:
    print('best case')
if e!=[]:
    print(e[0])
elif f==[]:
    print('worst case')