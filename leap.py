def leapyear(n):
    if(n%4==0):
        if(n%100==0):
            return n%400==0
        return True
    else:
        return False

c=1
while c==1:
    num=int(input('Enter any number ='))
    if(leapyear(num)):
        print(f'{num} is leap year')
    else:
        print(f'{num} is not leap year')
    c=int(input('Enter 1 to contine 0 to exit  ='))