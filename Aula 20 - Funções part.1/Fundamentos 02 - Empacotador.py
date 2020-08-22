def contador(*num): #Quando tiver '*' antes da variável ela pode receber qntd ilimidada de valores
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador(2,1,7,6,334)