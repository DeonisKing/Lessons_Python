def fib(num):
    f1 = 0
    f2, f3 = 0, 1
    f4 = 0
    while f4 < num:
        f1 += f3
        f2, f3 = f3, f2 + f3
        f4 += 1
    return f1
        
print(fib(int(input('Введите число фибоначчи:'))))
