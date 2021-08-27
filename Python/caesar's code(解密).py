P = input('please input your cipher text here:')
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CBA = "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"
u = len(P)
for i in range(u):
    s = P[i]
    if s in CBA:
        n=CBA.index(s)
        print(ABC[n],end='')
    else:
        print(s,end='')
