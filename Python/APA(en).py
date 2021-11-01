af=input('please input the first name of the author:')
am=input('please input the middle name of the author:')
al=input('please input the last name of the author:')
pt=al+','+af[0]+'.'+am[0]+'.,'
ask=input('Do you have another author?(Y/N):')
while ask == 'Y':
    af1=input('please input the first name of the author:')
    am1=input('please input the middle name of the author:')
    al1=input('please input the last name of the author:')
    pt=pt+al1+','+af1[0]+'.'+am1[0]+'.,'
    ask=input('Do you have another author?(Y/N):')
else:
    y=input('please input the year here:')
    n=input('please input the name of the publication:')
    p=input('please input the publisher:')
    pt=pt+'('+y+').'+n+', '+p+'.'
print(pt)
