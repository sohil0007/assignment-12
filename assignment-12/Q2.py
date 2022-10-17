num = int(input('Enter a number :'))

for e in range(2,num):
    if num%e==0:
        print('Not Prime Number')
        break

else:
    print('Prime Number')