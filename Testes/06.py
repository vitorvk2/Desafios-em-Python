print('Conversor de Medidas')
print(' ')

x = int(input('Valor em Metros:'))

cm = int(x*100)
mm = int(x*1000)

print('A conversão de {} metros para Centímetros e Milímetros ficou: {} Cm e {} MM'.format(x, cm, mm))