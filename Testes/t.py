a = []

for i in range(3):
    a.append(int(input('Número:')))

for i in range(3):
    if i == 0:
        maior = menor = a[i]
    else:
        if maior < a[i]:
            maior = a[i]
        if menor > a[i]:
            menor = a[i]

print(maior, menor)