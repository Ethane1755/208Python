r = input()
r = r.split()
d = []

for j in range(int(r[0]),int(r[-1])+1):
    b = len(str(j))
    a1 = [int(x) for x in str(j)]
    c = []
    for i in a1:
        c.append(i**b)
    if str(sum(c)) == str(j):
        d.append(str(j))
if d != []:
    print(' '.join(d))
if d == []:
    print('none')