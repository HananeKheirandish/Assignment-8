n = int(input('Please enter num: '))
for i in range(n*2-1):
    for j in range(n*2-1):
        if (i<n-1) and ((j+i < n-1) or (j-i > n-1)):
            print(' ' , end = '')
        elif (i>n-1) and ((i-j>n-1) or (i+j>(2*n)+(n-3))):
            print(' ' , end = '')
        else:    
            print('*' , end='')
    print()