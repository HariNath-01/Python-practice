totalbillamount=(int(input('enter total bill=')))
noofpeople=int(input('enter no of people='))
tip_per=int(input('enter tip percent='))
 
total=totalbillamount*tip_per/100

print(f'Amount each person shuold pay is{total/noofpeople}')