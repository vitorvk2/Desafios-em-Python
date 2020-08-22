cont = soma = 0

while True:
    num = int(input('Digite um número (999 para parar):'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de números digitados foi {cont} e a soma total entre eles é {soma}')