numer1 = int(input('Please enter numerator1: '))
deno1 = int(input('Please enter Denominator1: '))
numer2 = int(input('Pleaseenter numerator2: '))
deno2 = int(input('Please enter Denominator2: '))

frac1 = {'numer' : numer1 , 'deno' : deno1}
frac2 = {'numer' : numer2 , 'deno' : deno2}

def sum(x , y):
    result = {}
    result['numer'] = x['numer'] * y['deno'] + x['deno'] * y['numer']
    result['deno'] = x['deno'] * y['deno']
    return result

def sub(x , y):
    result = {}
    result['numer'] = x['numer'] * y['deno'] - x['deno'] * y['numer']
    result['deno'] = x['deno'] * y['deno']
    return result

def mul(x , y):
    result = {}
    result['numer'] = x['numer'] * y['numer']
    result['deno'] = x['deno'] * y['deno']
    return result

def divide(x , y):
    result = {}
    result['numer'] = x['numer'] * y['deno']
    result['deno'] = x['deno'] * y['numer']
    return result

while True:
    print('1- sum of fractions ')
    print('2- subtract of fractions ')
    print('3- multiply of fractions ')
    print('4- divide of fractions ')
    print('5- exit ')
    n = int(input('Choose which one: '))
    if n == 1:
        ans = sum(frac1 , frac2)
        print('Sum is: ' , ans['numer'] , '/' , ans['deno'])
    elif n == 2:
        ans = sub(frac1 , frac2)
        print('Subtract is: ' , ans['numer'] , '/' , ans['deno'])
    elif n == 3:
        ans = mul(frac1 , frac2)
        print('Multiply is: ' , ans['numer'] , '/' , ans['deno'])
    elif n == 4:
        ans = divide(frac1 , frac2)
        print('Divide is: ' , ans['numer'] , '/' , ans['deno'])
    elif n == 5:
        exit()
    else:
        print('Wrong choice! Try again.')