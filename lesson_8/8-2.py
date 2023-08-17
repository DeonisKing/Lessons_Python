import time
second=int(input('Введите интервал в секундах: '))
"""Функция выполняется 5 раз,интервал можете указать сами"""
def limiter(second):
    def decor(func):
        def wrap(*args,**kwargs):
            a=0
            while a<5:
                a+=1
                result=func(*args,**kwargs)
                time.sleep(second)
            return result
        return wrap
    return decor

@limiter(second)
def function():
    print('Функция')
function()

