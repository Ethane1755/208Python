#INPUT
a=input()
b,c=a.split()
b=int(b)
c=int(c)
d=input()
d=d.split()
d=list(map(int,d))
#VARIBLE K IS BALANCE
x=d[0]
#DROP D[0]
d.remove(d[0])
#DECIDE IF HAS MONEY
m=0
#START TRANSACTION
m=1
for i in d:
    #SELL
    if i>x+c:
        x=-x+i
        m=0
    #BUY
    elif m==0 and i<=x-c:
        x=i
        m=1
    print(x,',',m)
print(x)
