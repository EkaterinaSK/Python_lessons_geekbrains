'''1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''
my_list = [8, 'мама', 8.4, 5, 'папа']
for i in my_list:
    print( i, type(i))

'''2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().'''
el_count = int(input('сколько элементов будет в списке?'))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input('Введите следующее значение списка'))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).
Напишите решения через list и через dict.
'''
''' черз список'''
seasons_list = ['зима', 'весна', 'лето', 'осень']
month = int(input('укажите номер месяца'))
if month ==1 or month == 12 or month == 2:
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
        print('так не бывает')
''' через словарь'''
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input('укажите номер месяца'))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
    print('так не бывает')

'''
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное,
выводить только первые 10 букв в слове.
'''
my_str = input('введите строку')
my_word = []
num = 1
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[i]}")
        num += 1
    else:
        print(f" {num} {my_word[i][0:10]}")
        num += 1

'''
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''
    my_list = [7, 5, 3, 3, 2]
    print(f'Рейтинг - {my_list}')
    digit = int(input('Введите число (111 - выход) '))
    while digit != 111:
        for el in range(len(my_list)):
            if my_list[el] == digit:
                my_list.insert(el + 1, digit)
                break
            elif my_list[0] < digit:
                my_list.insert(0, digit)
            elif my_list[-1] > digit:
                my_list.append(digit)
            elif my_list[el] > digit and my_list[el + 1] < digit:
                my_list.insert(el + 1, digit)
        print(f'текущий список - {my_list}')
        digit = int(input('Введите число '))