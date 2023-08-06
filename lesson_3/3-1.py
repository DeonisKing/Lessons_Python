a = int(input("Введите число: "))
b = 1
while a > 1:
    b *= a
    a -= 1
    print(a, '=' ,b)