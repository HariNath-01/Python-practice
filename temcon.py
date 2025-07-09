#cel to for
# (0°C × 9/5) + 32 = 32°F -- for 0 deg celcious
temp=int(input('Enter temperature in celcious = '))
def celtofor(temp):
        print(int((temp*9/5)+32))
celtofor(temp)

#cel to kel
#0°C + 273.15 = 273.15K -it will take the celcious as input
temp=int(input('Enter temperature in celcious = '))
def celtokel(temp):
        print(int(temp+273.15))
celtokel(temp)

#far to cel
#(32°F − 32) × 5/9 = 0°C -- 32 deg far
temp=int(input('Enter temperature in Farhene = '))
def fartocel(temp):
        print(int((temp-32)*5/9))
fartocel(temp)

#far to kel
#(32°F − 32) × 5/9 + 273.15 = 273.15K -it will take the far value
temp=int(input('Enter temperature in Farhene = '))
def fartokel(temp):
        print(int((temp-32)*5/9 +273.15))
fartokel(temp)

#kel to cel
#0K − 273.15 = -273.1°C -- give the kel value input
temp=int(input('Enter the kelvin value ='))
def keltocel(temp):
    print(int(temp-273.15))
keltocel(temp)

#kel to far
#(0K − 273.15) × 9/5 + 32 = -459.7°F --give kel input
temp=int(input('enter the kel value ='))
def keltofar(temp):
    print(int((temp-273.15)*9/5+32))
keltofar(temp)