num = int(input('Enter a Number :'))
c=2
while num!=0:
    for i in range(2,c):
        if c%i==0:
            break
    else:
        print(c,end=' ')
        num-=1
    c+=1        