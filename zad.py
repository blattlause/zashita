import numpy as np
import random

from func import *

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
        operation(max_count, array)
        print("Новый массив")
        print(array)
    elif n == 2:
        inputt(max_count, array)
        print("Старый массив")
        print(array)
        operation(max_count, array)
        print("Новый массив")
        print(array)
    elif n == 3:
        flag = 0



