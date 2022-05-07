a=int(input())
b=int(input())
d=input()
c=d.split()
c=list(map(int,c))

def rps(k):
    if k==0:
        return 5
    if k==2:
        return 0
    if k==5:
        return 2

def race(m,n):
    if m==n:
        return 'Draw'
    if m==5 and n==2:
        return 'Lose'
    if m==5 and n==0:
        return 'Win'
    if m==2 and n==5:
        return 'Win'
    if m==2 and n==0:
        return 'Lose'
    if m==0 and n==2:
        return 'Win'
    if m==0 and n==5:
        return 'Lose'

first=race(a,c[0])
k=c[0]
c1=c
c.remove(c[0])
if first=='Win':
    print('won at round 1')
if first=='Lose':
    print('lost at round 1')
if first=='Draw':
    for i in c:
        if c.index(i)<2:
            a=k
        elif c1[c1.index(i)-1]==c1[c1.index(i)-2]:
            a=rps([c1.index(i)-1])
        else:
            a=c1[c1.index(i)-1]
        print(a)
        p=race(a,i)
        print(p)
        if p=='Win':
            print('won at round',c.index(i)+2)
            break
        if p=='Lose':
            print('lost at round',c.index(i)+2)
            break
        if c.index(i)==b-2 and p=='Draw':
            print('draw at round',len(c))