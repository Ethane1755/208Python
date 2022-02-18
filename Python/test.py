print('Please use Engish to answer the questions below.')
name=input('What is your name? ')
print('Hello,',name)
life=input('Do you like your life in CK?(Y/N)')
if life=='Y':
    print('Wow, me too!')
    express_free=input('Can you try to express yourself freely in CK?(Y/N)')
    if express_free=='Y':
        print('Have a good time here.')
    elif express_free=='N':
        print('Find yourself clubs and monkeys to entertain.')
    else:
        print('How do you find a solution not Y nor N?')
else:
    print('What make you hate CK?')
    hate_why=input('Can you tell me why?')
    if 'girl' in hate_why:
        print('What about TFG?')
        prefer=input('which do you prefer, TFG or ZS or?')
        if 'TFG' in prefer or 'ZS' in prefer:
            print('I see.')
        else:
            print(prefer, 'is better, then.')
    if 'CG' in hate_why:
        print("Don\'t care about strawberries.")
    else:
        happy=input('So you can not be happy here at CK?')
        happy_lw=happy.lower()
        if 'yes' in happy_lw:
            print('Go conseling immediately.')
        if 'no' in happy_lw:
            print('I guess you will only have an average life here.')
        else:
            print("I can\'t solve your problems here then.")
print('Thank you for your time.')