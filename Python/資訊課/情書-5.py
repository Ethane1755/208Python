s=str(input())

k=s.replace("_"," ")

c=k.split()

for index, value in enumerate(c):
    if value == 'i':
        c[index] = "I"

l=" ".join(c)
print(l)