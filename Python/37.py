grade={'number':[],'A':[],'B':[],'C':[]}

for i in range(5):
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())

    grade['number'].append(a)
    grade['A'].append(b)
    grade['B'].append(c)
    grade['C'].append(d)
    print(grade)
i=1
avg=[]
for j in range(5):
    print('student',i)
    print('1:',round(grade['A'][i-1],2))
    print('2:',round(grade['B'][i-1],2))
    print('3:',round(grade['C'][i-1],2))
    print('sum:',round(grade['A'][i-1]+grade['B'][i-1]+grade['C'][i-1],2))
    print('avg:',round((grade['A'][i-1]+grade['B'][i-1]+grade['C'][i-1])/3,2))
    avg.append(round((grade['A'][i-1]+grade['B'][i-1]+grade['C'][i-1])/3,2))
    i=i+1

print('total:',sum(grade['A'])+sum(grade['B'])+sum(grade['C']),', avg:',round((sum(grade['A'])+sum(grade['B'])+sum(grade['C']))/15,2))
print('highest avg:','student',avg.index(max(avg))+1,':',round(max(avg),2))