# import lesson5modules\main.py
import os
import sys

#sys.path.append('lesson5modules')
from lesson5modules.famous_info import fp
import lesson5modules.famous_info_copy

sys_files={'.git','.idea','lesson5modules','LICENSE','new.py','oo.py','other.py','venv'}

# print('hello')
# print('World')

val = 0
print('__name__',__name__)

while val == 0:
    print('Главное меню')
    print('''1. создать папку;
2. удалить (файл/папку);
3. копировать (файл/папку);
4. просмотр содержимого рабочей директории;
5. посмотреть только папки;
6. посмотреть только файлы;
7. просмотр информации об операционной системе;
8. создатель программы;
9. играть в викторину;
10. мой банковский счет;
11. смена рабочей директории (*необязательный пункт);
x. выход.''')
    val = input('?')
    print(val)
    if (val=='1'):
        print('Создаём папку:')
        dirname=input('Введите название папки:')
        try:
            os.mkdir(dirname)
            print(f'Папка {dirname} создана')
        except:
            print(f'Невозможно создать {dirname}')
    if (val=='2'):
        print('Удалить какой файл?')
        list=os.listdir('./')
        for i in list:
            if (i not in sys_files):
                print(i)
        file=input('Имя файла для удаления:')
        try:
            os.remove(file)
            # TODO: Сделать удаление директорий, сейчас работает только на файлы
            print(f'Ошибка удаления файла ', file)
        except:
            print(f'Ошибка удаления файла {file}')

    if val != 'X' and val != 'x' and val != 'Ч' and val != 'ч':
        val = 0
    # fp()
print (fp())