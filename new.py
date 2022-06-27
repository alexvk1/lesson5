# import lesson5modules\main.py
import sys

sys.path.append('lesson5modules')
from famous_info import fp
import famous_info_copy

# print('hello')
# print('World')

val = 0
print('Go now')
while val == 0:
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
        print('Создаём папку')

    if val != 'X' and val != 'x' and val != 'Ч' and val != 'ч':
        val = 0
    # fp()
print (fp())