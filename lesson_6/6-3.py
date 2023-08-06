a = int(input('Что хотите ввести?\n1-Радиус,2-Диаметр: '))
def rad():
    print('Длинна окружности = ', 2 * 3.14 * radius)
    print('Площадь = ',3.14 * radius ** 2)
def diam():
    print('Длинна окружности = ',2 * 3.14 * (diametr / 2))
    print('Площадь = ',3.14 * (diametr / 2) ** 2)
if a == 1:
    radius = int(input('Введите радиус: '))
    rad()
else:
    diametr = int(input('Введите диаметр: '))
    diam()