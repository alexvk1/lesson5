"""
Программа выводит год рождения случайного известного человека
"""
# from tkinter import *

# Импор всех функций из модуля
#from famous_persons import *

# Импорт нужных функций
from famous_persons import get_random_person as gr

def fp():
    #name, date = get_random_person()
    name, date = gr()
    print(name, date)
