a = int(input('Enter First Number :'))
b = int(input('Enter Second Number :'))

for m in range(1,a*b +1):
    if m%a==0 and m%b==0:
        print('LCM of number is ',m)
        break
