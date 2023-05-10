# Задача 30:  Заполните массив элементами арифметической прогрессии 
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно 
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9
# a1 = int(input(" Enter number a1: "))
# d = int(input(" Enter number d: "))
# n = int(input(" Enter number n: "))
# arr = [a1+i*d for i in range(n)]
# print(*arr, sep=', ')

# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
#  заданного максимума)
# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)

arr = [1, 3, 7, 10, 5, 8]
a = int(input("Enter the beginning of the range: "))
b = int(input("Enter the end of the range: "))
indices = [i for i in range(len(arr)) if a <= arr[i] <= b]
result = ",".join([f"{i}({arr[i]})" for i in indices])
print(result) 
