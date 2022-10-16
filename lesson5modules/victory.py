"""
Программа викторина будет задавать нам вопросы несколько раз
"""
# 1. Импорт конкретных функций из модуля
# from <название модуля> import нужные функций через ,
from lesson5modules.famous_persons import get_random_person, get_person_and_question

def vv():
    rounds = int(input('Сколько раз вы хотите играть?'))

    for i in range(rounds):
        get_person_and_question()

    print('Пока!')
