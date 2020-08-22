from time import sleep
from random import randint

def maior(*num):
    nummaior = 0
    print('\nAnalisando os valores passados...')
    for i in range(len(num)):
        print(f'{num[i]}  ',end='',flush=True)
        sleep(0.4)

        if i == 1:
            nummaior = num[i]
        else:
            if nummaior < num[i]:
                nummaior = num[i]
    print(f'O maior número é {nummaior}')


maior(10,453,5435,2,123,1436,342,4124,234,36,345,3)



