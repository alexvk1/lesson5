# import lesson5modules\main.py
import os
import shutil
import platform
import sys

#sys.path.append('lesson5modules')
from lesson5modules.famous_info import fp
import lesson5modules.famous_info_copy

sys_files={'.git','.idea','lesson5modules','LICENSE','new.py','oo.py','other.py','venv'}

# print('hello')
# print('World')

val = 0
print('__name__',__name__)

def list_dir(typ='a'):
    for filename in os.listdir('.'):
        if (filename not in sys_files):
            show_name=False
            if (typ=='a'):
                show_name=True
            if (typ=='d'):
                if os.path.isdir('./'+filename):
                    show_name=True
            if (typ=='f'):
                if os.path.isfile('./'+filename):
                    show_name=True
            if (show_name==True):
                print(f'{filename}')


while val == 0:
    print('Главное меню (22-10-15 20:22)')
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
    print(val+'\n----НАЧАЛО РАБОТЫ----')
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
        err=0 #0-нет ошибок, 1-каталог, 2-не получилось удалить
        try:
            os.remove(''+file)

            print(f'Файл {file} удалён')

        except:
            err=1
        if (err==1):
            print('Удаляем каталог')
            if (os.path.isdir(file)):
                try:
                    os.rmdir(file)
                    err=0
                except:
                    err=2

        if (err==0):
            print(f'Каталог {file} удалён')
        elif (err==2):
            print(f'Невозможно удалить {file}')
    if (val=='3'):
        print('Список папок и файлов:')
        list_dir()
        file = input('Скопировать что?')
        if (os.path.exists(file)):
            print('Сейчас как скопирую...')
            new_name=input('Новое имя файла:')
            err=False
            if (os.path.isdir(file)):
                try:
                    shutil.copytree(file,new_name)
                except:
                    err=True
            if (os.path.isfile(file)):
                try:
                    val=shutil.copy(file,new_name)
                except:
                    err=True
            if (err==True):
                print('Произошла ошибка')
            else:
                print('Скопировано')
        else:
            print('Имя файла неверное')


    if (val=='4'):
        list_dir()
    if (val=='5'):
        list_dir(typ='d')
    if (val == '6'):
        list_dir(typ='f')
    if (val == '7'):
        print(platform.system())
        print(platform.version())
        uname_res=platform.uname()
        print(uname_res)
    if (val == '8'):
        print('Кошкин Александр')
    if (val == '9'):
        from lesson5modules.victory import vv
        try:
            vv()
        except:
            print('Что-то пошло не так...')
    if (val == '10'):
        from baccount import start_baccount
        start_baccount()
    if (val == '11'):
        print('Текущий каталог:'+os.getcwd())
        new_path=input('Новый текущий каталог')
        os.chdir(new_path)
        os.getcwd()
    if val != 'X' and val != 'x' and val != 'Ч' and val != 'ч':
        val = 0
    # fp()
    print(f'-----КОНЕЦ РАБОТЫ-----')
print ('Завершение работы с программой')