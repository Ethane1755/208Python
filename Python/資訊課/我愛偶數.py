c=input()
a,b=c.split()
a=int(a)
b=int(b)
d=list()

def test(num):
    if (num % 2) == 0:
        return True
    else:
        return False

for i in range(a, b+1):   
    i_is_prime = test(i) 
    if i_is_prime:
        d.append('')

print(len(d))