
while True:
    num = int(input('Digite um número para ver a tabuada dele:'))
    if num > 0:
        for tab in range(1,11):
            print(f'{(num)} X {(tab)} = {(num*tab)}')
    else:
        break
