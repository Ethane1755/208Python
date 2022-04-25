a=input()
b=list(a)
b=list(map(int,b))
print(abs(sum(b[::2])-sum(b[1::2])))
