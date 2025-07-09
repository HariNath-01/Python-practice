format=int(input('Enter which format does pattern need to print'))
n=int(input('number of lines in pattern'))

if(format == 1):
    for i in range(1,n+1):
        j=i
        while j > 0:
            print("*",end="")
            j-=1
        print()
else:
    for i in range(1,n+1):
        j=n-i+1
        while j > 0:
            print("*",end="")
            j-=1
        print()