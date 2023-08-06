lst_str=input('Введите  числа через пробел: ').split()
lst_2=[float(n) if '.' in n else int(n) for n in lst_str]
def odd(a):
    if a % 2 == 0:
        return a
odd_numbers=list(filter(odd,lst_2))
def even(b):
    if b % 2 != 0:
        return b
even_numbers=list(filter(even,lst_2))
lst_3=even_numbers+odd_numbers
print(lst_3)






