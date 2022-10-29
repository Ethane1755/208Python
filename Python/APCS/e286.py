a = input()
b = input()
c = input()
d = input()

a = a.split()
b = b.split()
c = c.split()
d = d.split()

a=list(map(int,a))
b=list(map(int,b))
c=list(map(int,c))
d=list(map(int,d))

print(str(sum(a))+":"+str(sum(b)))
print(str(sum(c))+":"+str(sum(d)))
if sum(a) > sum(b) and sum(c) > sum(d):
    print('Win')
if sum(a) < sum(b) and sum(c) < sum(d):
    print('Lose')
if sum(a) == sum(b) and sum(c) == sum(d):
    print('Tie')