def getNumber ():
    flag = 1
    while flag == 1:
        number = int(input('Введите число: '))
        if number > 0 and number < 4 :
            return number
        else: print("Ошибка: введите чиcло из диапозона [1; 3]")

def inputt(max_count, array):
    for i in range(max_count):
        array[i] = int(input("Введите элемент массива: "))

def operation(max_count, array):
    min_index = 0
    for i in range(max_count):
        if array[i] < array[min_index]:
            min_index = i
    if min_index-3 < 0:
        print("Ошибка: индекс для минимального числа меньше трех")
    else:
        array[min_index-3] = array[min_index]
        array[min_index] = 101
