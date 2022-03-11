c=input()
a,b,d=c.split()
a=int(a)
b=int(b)
d=int(d)

def AND(a,b,d):
    if a!=0 and b!=0 and d==1 or a==0 and b==0 and d==0 or a==0 and b!=0 and d==0 or a!=0 and b==0 and d==0:
        print('AND')
        return True
def OR(a,b,d):
    if a==0 and b==0 and d==0 or a==0 and b!=0 and d==1 or a!=0 and b==0 and d==1 or a!=0 and b!=0 and d==1:
        print('OR')
        return True
def XOR(a,b,d):
    if a==0 and b==0 and d==0 or a==0 and b!=0 and d==1 or a!=0 and b==0 and d==1 or a!=0 and b!=0 and d==0:
        print('XOR')
        return True

x=AND(a,b,d)
y=OR(a,b,d)
z=XOR(a,b,d)

if not x and not y and not z:
    print('IMPOSSIBLE')








