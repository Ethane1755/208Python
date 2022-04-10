a=int(input())

if a<1000:
    b=a
    c=a
elif 1000<a<2000:
    b=a-100
    c=a
else:
    b=(a//1000)*(-100)+a
    c=(a//2000)*(-200)+a

if c>b:
    print(b,'1')
else:
    print(c,'0')
