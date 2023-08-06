x=int(input('Введите цену товара:'))
y=5
if x>100:
    y=10
if x>200:
    y=20
if x>300:
    y=25
print(x-x/100*y,'Руб')
print(y,'%')