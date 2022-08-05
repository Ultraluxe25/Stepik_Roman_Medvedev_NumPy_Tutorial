# Task 1. Напишите функцию, которая возвращает numpy массив на основе предложенного списка (lst).

import numpy as np

def solution(lst):
    arr = np.array(lst)
    return arr
    


# Task 2. Напишите функцию, которая возвращает одномерный массив длинной 100 и заполненный нулями.

import numpy as np

def solution():
    arr = np.zeros(100)
    return arr
    

# Task 3. Создайте массив заполненный нулями у которого shape = (2, 5)

import numpy as np

def solution():
    arr = np.zeros((2, 5))
    return arr


# Task 4. Создайте массив заполненный единицами у которого 5 строк и 8 столбцов (5 вложенных массивов длинной 8)

import numpy as np

def solution():
    arr = np.ones((5, 8))
    return arr
    
    
# Task 5. Создайте одномерный numpy массив со значениями 0, 1, 2, .... 99 (диапазон значений от 0 до 99)

import numpy as np

def solution():
    arr = np.arange(100)
    return arr
    
    
# Task 6. Создайте двумерный массив размером 5 х 2, который полностью будет заполнен значением 'G'

import numpy as np

def solution():
    arr = np.full((5, 2), 'G')
    return arr
    
    
# Task 7. Напишите функцию, которая на основе существующего списка создает numpy массив с типом float64

import numpy as np

def solution(lst):
    arr = np.array(lst, dtype='float64')
    return arr
    
    
# Task 8. К вам в распоряжение поступает массив arr с типом float64. Преобразуйте, пожалуйста, в int32

import numpy as np

def solution(arr):
    arr = arr.astype('int32')  # arr.astype(np.int32)
    return arr
    
    
""" Task 9. На вход подается одномерный массив со значениями от 0 до 5 (включительно).
# Примените некоторую операцию  чтобы на выходе получился массив со значениями 1000, 1001....1005 """

import numpy as np

def solution(arr):
    # если вдруг массив пришел с ошибкой, то можно
    # применить try/except или np.array(arr)
    # я же просто создаю свой массив
    arr = np.arange(6)  
    arr += 1000
    return arr
    
    
""" Task 10. На вход подается одномерный массив в котором хранится информация о количестве картофеля на каждом складе (всего 4 склада). 
Посчитайте для каждого склада, сколько процентов картофеля от общего количества хранится на каждом складе.
Общее количество картофеля на всех складах 115 кг
Не забудьте что каждое значение надо умножить на 100.
Округлять значения не требуется! Знак процента тоже добавлять не следует. Просто выполните арифметические операции. """

import numpy as np

def solution(arr):
    # print(arr) для просмотра arr = [10 25 15 50 15]
    # оказывается что складов 5)
    arr = np.array(arr)  # на случай, если передан список, а не массив
    arr = arr / 115
    arr *= 100
    return arr
