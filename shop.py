items = []
def add_items(val):
    items.append(val)
def view_cart():
    print(items)
def total_price():
    s = 0
    for i in items:
        s+=i[1]
    print(f'total price in cart is {s}')

while True:
    choice=int(input('1.Add item \n 2.View crt Item \n 3.calculate total price \n 4.exit \n Enter the choice ='))
    if(choice == 1):
        name=input('Enter nam eof item')
        price=int(input('Enter price of item'))
        add_items([name,price])
    elif(choice == 2):
        view_cart()
    elif(choice == 3):
        total_price()
    else:
        break