from random import randint
from time import sleep
comp = randint(0, 5) #Pensando

print('-=-'*20)
print('Pensarei em um número entre 0 e 5. Tente advinhar.')
print('-=-'*20)

jog = int(input('Em que número pensei?\n'))
print('PROCESSANDO...')

sleep(3)

if comp == jog:
    print('Você acertou!')

else:
    print('Você errou, tente novamente!')
