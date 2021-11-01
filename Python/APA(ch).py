a=input('請輸入作者全名:')
pt=a

ask=input('Do you have another author?(Y/N):')
while ask == 'Y':
    a=input('請輸入作者全名:')
    pt=pt+'、'+a
    ask=input('Do you have another author?(Y/N):')
else:
    y=input('請輸入年分:')
    n=input('請輸入文章名稱:')
    p=input('請輸入出版社:')
    pt=pt+'('+y+')。'+n+'，'+p+'。'
print(pt)
input()