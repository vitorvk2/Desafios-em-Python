import math

ang = float(input('Digite um ângulo:'))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O Ângulo de {(ang)}° possui \nSeno: {(seno):0.2f}, Cosseno: {(cos):0.2f}, Tangente: {(tan):0.2f}')