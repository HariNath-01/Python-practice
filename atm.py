balance = 3900
while True:
    choice=int(input('1.Check balance \n 2.Deposit money \n 3.withdraw money \n 4.eit \nEnter the choice='))
    if(choice == 1):
        print(f'balance is {balance}')
    elif(choice == 2):
        n=int(input('enter money todeposit ='))
        balance+=n
    elif(choice == 3):
        n=int(input('Money to with draw ='))
        if(balance < n):
            print(f'Insufficent balance,available balance is only {balance}')
        else:
            balance-=n
            print('payment successfull')
    else:
        break