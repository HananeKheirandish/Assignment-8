a = int(input('Please enter real1(a): '))
b = int(input('Please enter illusive1(b): '))
c = int(input('Pleas enter real2(c): '))
d = int(input('Please enter illussive(d): '))

complex1 = {'r' : a , 'i' : b}
complex2 = {'r' : c , 'i' : d}

def sum_complex(c1 , c2):
    result = {}
    result['r'] = c1['r'] + c2['r']
    result['i'] = c1['i'] + c2['i']
    return result

def mul_complex(c1 , c2):
    result = {}
    # (ac – bd) + (ad + bc)i
    result['r'] = c1['r'] * c2['r'] - c1['i'] * c2['i']
    result['i'] = c1['r'] * c2['i'] + c1['i'] * c2['r']
    return result

def sub_complex(c1 , c2):
    result = {}
    result['r'] = c1['r'] + -1 * c2['r']
    result['i'] = c1['i'] + -1 * c2['i']
    return result

def show_ans(r):
    if r['i'] >= 0: 
        print(r['r'] , '+' , r['i'] , 'i')
    else:
        print(r['r'] , r['i'] , 'i')

while True:
    print('1- Sum')
    print('2- Multiply')
    print('3- Subtract')
    print('4- exit')
    choice = int(input('Choose which one: '))
    if choice == 1:
        res = sum_complex(complex1 , complex2)
        show_ans(res)
    elif choice == 2:
        res = mul_complex(complex1 , complex2)
        show_ans(res)
    elif choice == 3:
        res = sub_complex(complex1 , complex2)
        show_ans(res)
    elif choice == 4:
        exit
    else:
        print('Wrong choice. Try again. ')