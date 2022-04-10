a=input()
b,c=a.split()
b=int(b)
c=int(c)

if b*2<=8*c<=b*3:
    print('Yes')
elif (8*c)<(b*2):
    print('Not Enough')
else:
    print('Too Much')
