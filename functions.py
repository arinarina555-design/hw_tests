'''
Напишите программу, которая проверяет вес посылки пользователя в килограммах (переменная weight).
Если вес не превышает 10 кг (включительно), выведите сообщение «Стоимость доставки: 200 руб.».
Если вес больше 10 кг, выведите сообщение «Стоимость доставки: 500 руб.».
Вес посылки может быть как целым числом, так и дробным.
'''
def get_cost(weight):
    if weight <= 10:
        result = 'Стоимость доставки: 200 руб.'
    else:
        result = 'Стоимость доставки: 500 руб.'
    return result




'''
Напишите программу, которая определяет самое длинное название фильма из предложенных.
'''
def longest_film(film_1: str, film_2: str, film_3: str) -> str:
    if len(film_1) > len(film_2) and len(film_1) > len(film_3):
        result = film_1
    elif len(film_2) > len(film_1) and len(film_2) > len(film_3):
        result = film_2
    elif len(film_3) > len(film_1) and len(film_3) > len(film_2):
        result = film_3
    elif len(film_1) == len(film_2) == len(film_3):
        result = 'все фильмы одинаковой длины'
    else:
        result = 'невозможно выбрать'
    return result




'''
Написать программу, которая шифрует входящие сообщения по такому правилу:
Если количество символов в сообщении чётное, то сообщение надо разделить ровно посередине 
и первую половину поместить в конец, а вторую — в начало.
Если количество символов в сообщении нечётное, то каждый второй символ надо переместить в новую строку. 
После чего новую строку с перемещёнными символами приклеить в конец к первой.
'''
def encrypt(text: str) -> str:
    first = ''
    second = ''
    if len(text)%2 == 0:
        a = len(text)//2
        result = text[-a:len(text)]+text[0:a]
    else:
        for i in range(len(text)):
            if i%2 == 0:
                first += text[i]
            else:
                second += text[i]
        result = first+second
    return result