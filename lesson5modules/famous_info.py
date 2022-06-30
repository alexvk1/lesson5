"""
Программа выводит год рождения случайного известного человека
"""
# from tkinter import *

# Импор всех функций из модуля
#from famous_persons import *

# Импорт нужных функций
from lesson5modules.famous_persons import get_random_person as gr

def fp():
    #name, date = get_random_person()
    name, date = gr()
    print(name, date)

if (__name__=='__main__'):
    print('__name__',__name__)