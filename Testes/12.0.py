import random
num = random.randint(1, 4)

aluno1 = input('Digite o nome do Primeiro:')
aluno2 = input('Digite o nome do Segundo:')
aluno3 = input('Digite o nome do Terceiro:')
aluno4 = input('Digite o nome do Quarto:')

print (' ')
print ('Aluno para o Trabalho')
if num == 1:
    print ('O aluno escolhido é: {}'.format(aluno1))

elif num == 2:
    print ('O aluno escolhido é: {}'.format(aluno2))

elif num == 3:
    print ('O aluno escolhido é: {}'.format(aluno3))

else:
    print ('O aluno escolhido é: {}'.format(aluno4))

print (' ')

num1 = random.randint(1,4)
num2 = random.randint(1,4)
num3 = random.randint(1,4)
num4 = random.randint(1,4)

if num1 == num2 or num1 == num3 or num1 == num4:
    num1 = random.randint(1,4)
    if num1 == num2 or num1 == num3 or num1 == num4:
        num1 = random.randint(1,4)

elif num2 == num1 or num2 == num3 or num2 == num4:
    num2 = random.randint(1,4)
    if num2 == num1 or num2 == num3 or num2 == num4:
        num2 = random.randint(1,4)

elif num3 == num4 or num3 == num2 or num3 == num1:
    num3 == random.randint(1,4)
    if num3 == num4 or num3 == num2 or num3 == num1:
        num3 == random.randint(1,4)

elif num4 == num3 or num4 == num2 or num4 == num1:
    num4 == random.randint(1,4)
    if num4 == num3 or num4 == num2 or num4 == num1:
        num4 == random.randint(1,4)


print ('Ordem de Apresentação')

if num1 == 1 or num1 == 2 or num1 == 3 or num1 == 4:
    if num1 == 1:
        pri = aluno1
    
    elif num1 == 2:
        pri = aluno2

    elif num1 == 3:
        pri = aluno3
    
    else:
        pri = aluno4


if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4:
    if num2 == 1:
        seg = aluno1
    
    elif num2 == 2:
        seg = aluno2

    elif num2 == 3:
        seg = aluno3
    
    else:
        seg = aluno4

if num3 == 1 or num3 == 2 or num3 == 3 or num3 == 4:
    if num3 == 1:
        ter = aluno1
    
    elif num3 == 2:
        ter = aluno2

    elif num3 == 3:
        ter = aluno3
    
    else:
        ter = aluno4

if num4 == 1 or num4 == 2 or num4 == 3 or num4 == 4:
    if num4 == 1:
        qua = aluno1
    
    elif num4 == 2:
        qua = aluno2

    elif num4 == 3:
        qua = aluno3
    
    else:
        qua = aluno4

print('Primeiro: {}, Segundo: {}, Terceiro: {}, Quarto: {}.'.format(pri,seg,ter,qua))