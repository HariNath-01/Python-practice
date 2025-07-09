def prime(n):
    if n <=1:
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
    
a=int(input('Enter first number'))
b=int(input('Enter second number'))

for i in range(a,b+1):
    if(prime(i)):
        print(i)