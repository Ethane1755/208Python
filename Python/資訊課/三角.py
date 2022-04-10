p=input()
a,b,c=p.split()
a=int(a)
b=int(b)
c=int(c)

d=max(a,b,c)
e=min(a,b,c)
f=a+b+c-d-e

print(e,f,d)
if e+f<=d:
    print('No')
elif e**2+f**2<d**2:
    print('Obtuse')
elif e**2+f**2==d**2:
    print('Right')
elif e**2+f**2>d**2:
    print('Acute')