n = int(input('Enter num for which table need to print'))
print('Enter range of table')

start = int(input('Enter from which table should start = '))
end = int(input('Enter which table should end = '))

for i in range(start,end+1):
    print(f'{n} * {i} = {n*i}')