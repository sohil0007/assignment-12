num = int(input('Enter a Number of terms of a Fibonacci series :'))
f1,f2=0,1
if num==0:
    print(f1)

elif num==1:
    print(f1,f2,sep=' ')

else:
    print(f1,f2,end=' ')
    for i in range(3,num+1):
        f3=f1+f2
        print(f3,end=' ')
        f1=f2
        f2=f3