a=input()
b=list(a)
b=list(map(int,b))
b.reverse()
c=list(b[::2])
print(sum(c))
