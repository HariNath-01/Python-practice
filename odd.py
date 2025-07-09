'''lst = input('Enter a list of numbers separated by commas (e.g., 1,2,3,4,...): ').split(',')

even = []
odd = []

for i in lst:
    try:
        val = int(i)  # Convert each item to an integer
        if val % 2 == 0:
            even.append(val)
        else:
            odd.append(val)
    except ValueError:
        print(f"'{i}' is not a valid number, skipping.")
        
print(f'Even list is {even}')
print(f'Odd list is {odd}')'''

lst=list(input('Enter list of numbers =').split(',')) #give in form of 1,2,3,4,5,6,...
# print(lst)
even=[]
odd=[]

for i in lst:
    val=int(i)
    if(val%2==0):
        even.append(val)
    else:
        odd.append(val)

print(f'Even list is {even}')
print(f'odd list is {odd}')
