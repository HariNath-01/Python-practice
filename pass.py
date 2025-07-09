password=input('enter password =')
if(len(password) >= 8):
    upper_letter=0
    lower_letter=0
    digit=0
    special=0


    for i in password:
        if(i>='a' and i<='z'):
            lower_letter+=1
        elif (i>='A' and i<='Z'):
            upper_letter+=1
        elif i>='0' and i<='9':
            digit+=1
        else:
            special+=1
    if upper_letter > 0 and lower_letter >0 and digit>0 and special>0:
        print('Password is strong')
    else:
        print('Password is not strong')
else:
    print('password should contain atleast 8 characters')