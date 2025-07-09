stu_name=input('Enter student name')
print('Enter marks of 5 subjects')
s=0
for i in range(0,5):
    marks=int(input(f'Enter marks of {i+1} subject'))
    s+=marks

print(f'Total marks are {s}')
percentage= (s/500)*100
print(f'percentage is {percentage} %')

if(percentage <= 34):
    print('fail')
elif(percentage > 34 and percentage<50):
    print('C grade')
elif(percentage >= 50 and percentage <= 85):
    print('B grade')
else:
    print('A grade')