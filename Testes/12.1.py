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

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(lista)