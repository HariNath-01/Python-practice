def vowels(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        return True 
    else:
        return False
str=input('Enter lower string to analyse =')
ipt=str.lower()

c_v=0
c_c=0
c_special=0
c_digit=0

for i in ipt:
    if(i>='a' and i<='z'):
        if(vowels(i)):
            c_v+=1
        else:
            c_c+=1
    elif i>='0' and i<='9':
        c_digit+=1
    else:
        c_special+=1

print(f'no of vowels are {c_v}')
print(f'no of consonents are {c_c}')
print(f'no of specila char are {c_special}')
print(f'no of digits are {c_digit}')
print(f'reverse of string is {str[::-1]}')
    