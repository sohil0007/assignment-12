num = int(input('Enter a number :'))

n = num+1

while n>0:
    for i in range(2,n):
        if n%i==0:
            n+=1
            break
    else:
        print(n)
        break