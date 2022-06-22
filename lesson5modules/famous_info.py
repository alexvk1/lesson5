"""
Программа выводит год рождения случайного известного человека
"""
# from tkinter import *

# Импор всех функций из модуля
from famous_persons import *

def fp():
    name, date = get_random_person()
    print(name, date)
