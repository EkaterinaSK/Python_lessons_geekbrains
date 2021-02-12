'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
'''

def my_func (arg1, arg2):
    try:
        res = arg1 / arg2
        return res
    except ZeroDivisionError:
        return "Ошибка! деление на 0"
print(my_func(int(input("Введите делимое ")), int(input("Введите делитель "))))

'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
firstname = input("enter name")
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')
def about_func(firstname, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(about_func(surname = 'Familyname', firstname = 'Name', year = '000', city = 'BigApple', email = 'error@mail.ru', telephone = '112'))

'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
def max_sum_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    return(sum(total))
print(max_sum_func(3,5,6))

'4. Программа принимает действительное положительное число x и целое отрицательное число y. '
'Необходимо выполнить возведение числа x в степень y. ' \
'Задание необходимо реализовать в виде функции my_func(x, y). П' \
'при решении задания необходимо обойтись без встроенной функции возведения числа в степень.'
def my_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans
print(my_func(int(input('введите число1:' )),int(input('в какую степень возводим? '))))

'''
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')

'''
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func() 