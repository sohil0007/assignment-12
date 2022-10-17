from math import gcd
num1 = int(input('Enter First Number :'))
num2 = int(input('Enter second Number :'))

if gcd(num1,num2)==1:
    print(num1,'&',num2,'are coprime')

else:
    print(num1,'&',num2,'are not coprime')    