import random
import time
random_number = random.randint(1,100)
random_number2 = random.randint(1000000,10000000)
a=0
start=time.time()
while a != 1000000:
    random_number ** random_number2
    a += 1
    end=time.time()
    print('Время выполнения цикла составляет: ',int(end),'Сек')
    