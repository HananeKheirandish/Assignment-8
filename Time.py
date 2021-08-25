time1 = input('Please enter time1-{hour:minute:second} : ')
time2 = input('Please enter time2-{hour:minute:second} : ')

time1 = time1.split(':')
time2 = time2.split(':')

time1 = {'h' : int(time1[0]) , 'm' : int(time1[1]) , 's' : int(time1[2])}
time2 = {'h' : int(time2[0]) , 'm' : int(time2[1]) , 's' : int(time2[2])}

def sum_time(t1,t2):
    result = {}
    result['h'] = t1['h'] + t2['h']
    result['m'] = t1['m'] + t2['m']
    result['s'] = t1['s'] + t2['s']
    return result

def sub_time(t1,t2):
    result = {}
    result['h'] = t1['h'] - t2['h']
    result['m'] = t1['m'] - t2['m']
    result['s'] = t1['s'] - t2['s']
    return result

def second_to_time():
    second = int(input("Please enter second: "))
    result = {}
    result['h'] = second / 3600
    result['m'] = (second % 3600) / 60
    result['s'] = (second % 3600) % 60
    return result

def time_to_second(t):
    second = t['h'] * 3600 + t['m'] *60 + t['s']
    print('Second: ' , second)

def show_time(res):
    if res['s'] >= 60:
        res['s'] -= 60
        res['m'] += 1
    if res['m'] >= 60:
        res['m'] -= 60
        res['h'] += 1
    if res['h'] >= 24:
        res['h'] -= 24
    if res['s'] < 0:
        res['m'] -= 1
        res['s'] += 60
    if res['m'] < 0:
        res['h'] -= 1
        res['m'] += 60
    if res['h'] < 0:
        res['h'] += 24
    print(str(int(res['h'])).zfill(2),":",str(int(res['m'])).zfill(2),":",str(int(res['s'])).zfill(2))

while True:
    print('1- sum of times ')
    print('2- submite of times ')
    print('3- second to time ')
    print('4- time to second ')
    print('5- exit ')
    choice = int(input('Please enter your choose: '))
    if choice == 1:
        res = sum_time(time1 , time2)
        show_time(res)
    elif choice == 2:
        res = sub_time(time1 , time2)
        show_time(res)
    elif choice == 3:
        res = second_to_time()
        show_time(res)
    elif choice == 4:
        time_to_second(time1)
        time_to_second(time2)
    elif choice == 5:
        exit()
    else:
        print('Wrong choice. Try again.') 