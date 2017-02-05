import math

x = input('x = ')
figure = input('figur = ')

try:
    x = float(x)
except:
    print('error')
    exit(1)

if x <= 0:
    print('error')
    exit(1)
elif figure == 'circle':
    S = math.pi * x**2
    print('S = %.2f' % S)
elif figure == 'square':
    S = x**2
    print('%.2f' % S)
else:
    print('error')
    exit(1)

