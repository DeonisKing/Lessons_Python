import os
def create_folder():
    if not os.path.isdir('folder'):
        os.mkdir('folder')
        """Создаем папку folder если её нету"""
    if not os.path.isdir('second'):
        os.mkdir('second')
        """Создаем папку second если её нету"""
    if not os.path.isdir('third'):
        os.mkdir('third')
        """Создаем папку third если её нету"""
    os.replace('6-1.py', 'folder/6-1.py')
    """Перемещает файл в папку folder"""
    os.chdir('folder')
    """Заходим в папку folder"""
    print('Мы находимся в ' + os.getcwd())
    """Наше местонахождение"""
create_folder()
exit =int(input('Отменить изменения?\n1 если Да,2 если Нет: '))
if exit == 1:
    """Отмена изменений"""
    os.replace('6-1.py', '../6-1.py')
    os.chdir('..')
    os.rmdir('folder')
    os.rmdir('second')
    os.rmdir('third')
    print('Мы находимся в ' + os.getcwd())
    """Наше местонахождение"""
else:
    print('Выход')
    
    





