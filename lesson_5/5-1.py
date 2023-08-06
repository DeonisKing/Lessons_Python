stroka='строка '
def s1():
    print('Это первый способ!')
    time=0
    while time<10:
        print(stroka)
        time+=1
def s2():
    print('Это второй способ!')
    for i in range(10):
        print(stroka)
def s3():
    print('Это третий способ!')
    print(stroka.replace(' ','\n')*10)
s1(),s2(),s3()



