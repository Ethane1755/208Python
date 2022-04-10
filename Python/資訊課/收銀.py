a=int(input())
b=int(input())

a=100-a
if b==50:
    print('0',a//10,(a%10)//5,(a%10)%5)
elif b==10:
    print(a//50,'0',(a%50)//5,(a%50)%5)
else:
    print(a//50,(a%50)//10,'0',(a%50)%10)

