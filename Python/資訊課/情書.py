###1
s=str(input())

s1 = s[:len(s)//2]
s2 = s[len(s)//2:]
print(s2+s1)
###2
str=s2+s1
length_str=len(str)
sliced_str=str[length_str::-1] 
print(sliced_str)
###3
letter=sliced_str
A=letter.replace('A','')
B=A.replace('B','')
C=B.replace('C','')
D=C.replace('D','')
E=D.replace('E','')
F=E.replace('F','')
G=F.replace('G','')
H=G.replace('H','')
I=H.replace('I','')
J=I.replace('J','')
K=J.replace('K','')
L=K.replace('L','')
M=L.replace('M','')
N=M.replace('N','')
O=N.replace('O','')
P=O.replace('P','')
Q=P.replace('Q','')
R=Q.replace('R','')
S=R.replace('S','')
T=S.replace('T','')
U=T.replace('U','')
V=U.replace('V','')
W=V.replace('W','')
X=W.replace('X','')
Y=X.replace('Y','')
Z=Y.replace('Z','')
print(Z)
###4
a=Z
b=a.replace("*","i")
c=b.replace("2","to")
print(c)
###5
s=c

k=s.replace("_"," ")

c=k.split()

for index, value in enumerate(c):
    if value == 'i':
        c[index] = "I"

l=" ".join(c)
print(l)
###end
k=". ".join([each.capitalize() for each in l.split(". ")])
c=k.split()

for index, value in enumerate(c):
    if value == 'i':
        c[index] = "I"

l=" ".join(c)
print(l)