eq = '4x^2 +4x +    (-8) =  0'

eq1 = eq.replace(' ', '').replace('+', '').replace('x', '').replace('^2', '').replace('(','')
eq2 = eq1.replace(')', '').replace('=0', '')

a = int(eq2[:1])
b = int(eq2[1:2])
c = int(eq2[2:])

x1 = int((-b + ((b**2 - 4*a*c) ** 0.5)) / (2*a))
x2 = int((-b - ((b**2 - 4*a*c) ** 0.5)) / (2*a))
print(x1, x2)