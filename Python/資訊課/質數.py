a=int(input())

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

i = 0
while (i<a):
    b=int(input())
    if b==1:
        print("N")
    if isitPrime(b):
        print("Y")
    else:
        print("N")
    i=i+1
