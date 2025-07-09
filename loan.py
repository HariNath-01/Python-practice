salary = int(input('Enter salary = '))
age = int(input('Enter age ='))
credit_score=int(input('enter credit score = '))

if salary < 1000000 and age >18 and credit_score >1000:
    print('loan is approved')
else:
    print('Bank loan is rejected,reasons are :')
    if (salary >= 1000000):
        print('salary is >=1000000,so loan is rejected')
    if (age<=18):
        print('age is <= 18,so loan is rejected')
    if (credit_score<=1000):
        print('credit_score is <=1000,so loan is rejected')