print ('Calculadora da Hipotenusa')
import math

c_a = float(input('Digite o Cateto Adjacente:'))
c_o = float(input('Digite o Cateto Oposto:'))

rca = float(c_a**2)
rco = float(c_o**2)
hp = float(rca+rco)
rhp = math.sqrt(hp)

print('A hipotenusa mede: {:.2f}'.format(rhp))