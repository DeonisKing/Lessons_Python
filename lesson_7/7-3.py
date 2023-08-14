import sys
def decor(func):
    def wrap(*args,**kwargs):
        sys.stdout= None
        func() 
        return func
    return wrap

@decor
def function():
    print('Данный текст будет удален')
function()