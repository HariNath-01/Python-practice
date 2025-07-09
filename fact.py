n=int(input('Enter number for which we need to find the factorial ='))

if(n < 0):
    print("For negative number we can't find the factorial")
elif(n==0):
    print('factorial of 0 is 1')
else:
    s=1
    for i in range(1,n+1):
        s*=i
    print(f"factorial of a number is {s}")