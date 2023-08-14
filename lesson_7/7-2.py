def decor(func):
    def wrap(*args,**kwargs):
        if not wrap.a:
            login=str(input("Введите логин: "))
            password=str(input("Введите пароль: "))
            if auto(login,password):
                wrap.a = True
            else:
                print("Неправильный логин или пароль!")
                return
        return func(*args,**kwargs)
    wrap.a=False
    return wrap


def auto(login,password):
    base={
        "kirill":"12345",
        "maks":"qwerty",
        "den":"sosiski",
    }
    return base.get(login)==password
@decor
def oper():
    print('ВЫПОЛНЯЮ ВХОД')
oper()


            
        
