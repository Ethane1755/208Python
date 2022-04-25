a=input()
a1,a2,a3,a4=a.split()
a1=int(a1)
a2=int(a2)
a3=int(a3)
a4=int(a4)
b=input()
b1,b2,b3,b4=b.split()
b1=int(b1)
b2=int(b2)
b3=int(b3)
b4=int(b4)
c=input()
c1,c2,c3,c4=c.split()
c1=int(c1)
c2=int(c2)
c3=int(c3)
c4=int(c4)
d=input()
d1,d2,d3,d4=d.split()
d1=int(d1)
d2=int(d2)
d3=int(d3)
d4=int(d4)

h1=a1+a2+a3+a4
h2=c1+c2+c3+c4
g1=b1+b2+b3+b4
g2=d1+d2+d3+d4

print(h1,':',g1,sep='')
print(h2,':',g2,sep='')

if h1>g1 and h2>g2:
    print('Win')
elif h1<g1 and h2<g2:
    print('Lose')
else:
    print("Tie")