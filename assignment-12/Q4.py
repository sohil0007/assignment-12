num1=int(input('Enter First Number :'))
num2=int(input('Enter second Number :'))
n=num1
while n<=num2:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
        print(n,end=' ')
    n+=1        
