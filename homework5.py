# Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
# def stepen(a, b):
#     if a == 0:
#         return 0
#     elif b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * stepen(a, b-1)
# a = int(input(" Enter number a: "))   
# b = int(input(" Enter number b: ")) 
# result = stepen(a, b)
# print(f"{a} to the extent {b} equals {result}") 
    
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
# *Пример:*
# 2 2
#     4
def sum(a, b):
    if b == 0:
        return a
    
    return sum(a+1, b-1)
a = int(input(" Enter number a: "))   
b = int(input(" Enter number b: ")) 
result = sum(a, b)
print(f"sum of numbers {a} and {b} equals {result}")

