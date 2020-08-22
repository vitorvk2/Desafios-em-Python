fat = 1
num = int(input('Digite o número FATORIAL:'))

if num >= 0:
    for i in range (num,1,-1):
        fat *= i
    print(fat)

else:
    print('Valor Inválido!')