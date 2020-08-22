def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos {s}')



soma(5,2,1,5,32,6,34)
soma(32,3,1,5,2)