def fact(n):
    """Вычисление факториала"""
    a = n
    b = 1
    while a > 1:
        b *= a
        a -= 1
    return b
print(fact(int(input('Введите число:'))))

