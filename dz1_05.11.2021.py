from math import pi,sqrt

# №1 - Радиус круга
r = int(input("Введите радиус круга :"))

s = pi * r**2

c = 2 * pi * r

print(f'Площадь круга = {s}, Длинна окружности = {c}\n')

# №2 а) - Площадь кольца
r = list(map(int, input("Введите радиусы кольца :").split()))

s = pi * abs(r[0]-r[1])**2

print(f'Площадь кольца :{s}\n')

# №2 б) - Площадь правильного треугольника
a = int(input("Введите сторону правильного треугольника :"))

s = a**2 * sqrt(3) / 4

print(f'Площадь треугольника :{s}\n') 

# №3 - Обмен значениями переменных
val1 = 0
val2 = 1
print(f'{val1=}, {val2=}')
val1, val2 = val2, val1
print(f'{val1=}, {val2=}\n')

# №4 - Возведение числа в 10 степень используя 4 умножения
val = int(input("Введите число для возведения в 10 степень :"))

x = val * val

y = x * x 

y = y * y 

x = y * x

print(f'{val} в 10 степени = {x}\n')

# №5 - 1_000_000 из 5 пятерок
print(f'(5+5)**5(5+5) = {(5+5)**5*(5+5)}')



