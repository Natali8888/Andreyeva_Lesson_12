#1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.
#def func(a, b):
#    return a+b
#print(func(75, 100))

# 2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.
#def spisok (A):
#     summa = 0
#     for i in A:
#         summa += int(i)
#     return summa/len(A)
#my_list = list(input("Введите числа: "))
#print("Среднее значение:", spisok(my_list))

# 3. Напишите функцию, которая принимает на вход число и возвращает True, если оно четное,
# и False, если оно нечетное.
#def number (a): return a % 2 == 0
#print(number(88))

# 4. Напишите функцию, которая принимает на вход список и возвращает новый список, содержащий
# только уникальные элементы из исходного списка.
#numbers = [2,7,7,8,8,9,9]
#def unic_numbers(numbers):
#    list_unic_numbers = []
#    unic_list_numbers = set(numbers)
#    for i in unic_list_numbers:
#        list_unic_numbers.append(i)
#    return list_unic_numbers
#print(unic_numbers(numbers))


# 5. Решите задачу с использованием вложенной функции is_square. Предположим, у нас есть список чисел и мы хотим найти все числа, которые являются квадратами других чисел в этом списке.
# Шаблон кода (ориентировачный):
#def find_square_numbers(numbers):
#    def is_square(number):
#        return number**0.5 in numbers
#    new_list = []
#    for i in numbers:
#        if is_square(i): new_list.append(i)
#    return new_list
#print(find_square_numbers([1,3,2,6,7,8,9]))

