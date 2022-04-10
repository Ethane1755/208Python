c=input()
a,b=c.split()
a=eval(a)
b=eval(b)

total=0

for x in range(a,b+1):
  if(x%2==0):
    total+=x

print(total)