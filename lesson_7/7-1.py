lst=[]
def my_decor(func):
    def wrap(*args,**kwargs):
        if func.__name__ in lst:
            print('Ошибка')
            return
        else:
            lst.append(func.__name__)
        return func(*args,**kwargs)
        
    return wrap
@my_decor
def function():
    print('Функция')
function()
function()
"""Проверка"""
function()
"""Дополнительная проверка"""
function()
"""Дополнительная проверка"""




