import numpy as np
import random

def getNumber ():
    flag = 1
    while flag == 1:
        number = int(input('Введите число: '))
        if number > 0 and number < 4 :
            return number
        else: print("Ошибка: введите чиcло из диапозона [1; 3]")

def inputt():
    for i in range(max_count):
        array[i] = int(input("Введите элемент массива: "))

def operation():
    min_index = 0
    for i in range(max_count):
        if array[i] < array[min_index]:
            min_index = i
    if min_index-3 < 0:
        print("Ошибка: индекс для минимального числа меньше трех")
    else:
        array[min_index-3] = array[min_index]
        array[min_index] = 101


max_count = 10
array = np.zeros(max_count)

flag = 1
while flag ==1:
    print("1 - рандомный ввод")
    print("2 - ввод вручную")
    print("3 - exit")
    n = getNumber();
    if n == 1:
        for i in range(max_count):
            array[i] = random.randint(0, 40)
        print("Старый массив")
        print(array)
        operation()
        print("Новый массив")
        print(array)
    elif n == 2:
        inputt()
        print("Старый массив")
        print(array)
        operation()
        print("Новый массив")
        print(array)
    elif n == 3:
        flag = 0



