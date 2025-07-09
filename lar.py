'''for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)'''

n = int(input('Enter number of elements in the list: '))

if n == 0:
    print('List does not contain any elements.')
else:
    lst = []
    for i in range(n):
        p = int(input('Enter number: '))
        lst.append(p)
    
    lst.sort()

    if n == 1:
        print('There is only one element in the list, so no second largest element.')
    else:
        print('Second largest number:', lst[-2])
