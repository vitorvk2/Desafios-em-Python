a = float(input('Altura em Metros:'))
l = float(input('Largura em Metros:'))

area = float(a*l)
tin = float(area/2)

print('A área total em M² é: {:.2f}, a quantidade total de baldes de tintas para pintar são: {:.2f}'.format(area,tin))