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


""" Task 11. Выполните действия
1)Создайте одномерный массив со значениями в диапазоне от 0 до 10 (включительно). 
2)Создайте второй одномерный массив со значениями в диапазоне от 10 до 20 (включительно). 
3)Вычтите из второго массива первый. 
4)Проверьте каждое значение получившегося массива на равенство значению 10. Результат сравнения верните в отдельном numpy массиве. """

import numpy as np

def solution():
    arr1 = np.arange(11)
    arr2 = np.arange(10, 21)
    arr3 = arr2 - arr1
    arr4 = arr3 == 10
    return arr4  # arr4.dtype == 'bool'


""" Task 12. Во входящем массиве arr содержится информация о водителях, которые превысили скорость на некотором участке дороги.
Определите насколько каждый водитель превысил скорость, если допустимая скорость равна 80.
Результаты представьте в отдельном numpy массиве """

import numpy as np

def solution(arr):
    arr = arr - 80
    return arr


""" Task 13. На вход вашей функции подается некоторый одномерный массив.
Предполагается, что там лежат числа с плавающей точкой, но записаны они как строка.
Выполните сложение элементов с индексами 1 и 3.
На выходе ваша функция должна вернуть число (сумма двух элементов массива). """

import numpy as np

def solution(arr):
    arr = arr.astype(np.float64)
    result = arr[1] + arr[3]
    # result = arr[[1, 3]].sum()
    return result


""" Task 14. На вход вашей функции подается два одномерных массива.
Сложите первые два элемента первого массива с последними двумя элементами второго массива (поэлементно).
На выходе должен получится новый одномерный массив, который будет хранить два значения: """

import numpy as np

def solution(arr1, arr2):
    arr = np.array([arr1[0] + arr2[-2], arr1[1] + arr2[-1]])
    # менее подробно arr = arr1[:2] + arr2[-2:]
    return arr


# Task 15. На вход подается некоторый одномерный массив. Занулите первые 3 элемента.

import numpy as np

def solution(arr):
    arr[:3] = 0
    return arr


# Task 16. На вход подается двумерный массив (матрица):
# https://ucarecdn.com/d2707fa4-3105-46da-a1d7-0a4ca4e40362/
# вытяните из матрицы указанную область.

""" arr для задач 16-24
arr = [[10, 12, 14, 18, 20],
       [ 8, 22, 18, 19, 12],
       [ 4, 14, 84, 38, 11],
       [ 2, 32,  4, 31,  9],
       [ 1, 11,  1,  8,  6]]
"""

import numpy as np

def solution(arr):
    arr = arr[:2, :2]
    return arr


# Task 17. На вход подается двумерный массив (матрица):
# https://ucarecdn.com/7f96bccf-dce4-430f-8f5e-9842a24b5000/
# вытяните из матрицы указанную область.

import numpy as np

def solution(arr):
    arr = arr[1:3, 3:]
    return arr


# Task 18. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/1d6c0c70-0f78-4827-8f21-072923404f5d/

import numpy as np

def solution(arr):
    arr = arr[:, 0] + arr[:, 3]
    return arr


# Task 19. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/7531165c-7236-4a03-af90-970f76bdf2e1/

import numpy as np

def solution(arr):
    arr = arr[1] + arr[3]
    return arr


# Task 20. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/7a2be0a9-154f-4324-a1c3-86413db31247/

import numpy as np

def solution(arr):
    arr = arr[1:4, 1] + arr[1:4, 3]
    return arr


# Task 21. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/2f1ff817-4521-44d2-8b96-bf866ef9e932/

import numpy as np

def solution(arr):
    arr = arr[0, :4] + arr[4, 1:]
    return arr


# Task 22. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/faa3d37f-a16c-49b0-aeb7-e45512d9dcf7/

import numpy as np

def solution(arr):
    arr = arr[1:4, 1] + arr[2:, 2]
    return arr


# Task 23. Выполните поэлементное сложение двух столбцов:
# https://ucarecdn.com/2bf71390-a37e-4420-a0e9-27f3b3ce6b06/

import numpy as np

def solution(arr):
    arr = arr[2:, :2] + arr[:3, 3:]
    return arr


# Task 24. ыполните поэлементное сравнение двух столбцов:
# https://ucarecdn.com/21f66abd-1a69-444c-9138-eeaf8d9d54de/
# если значение в первом столбце больше чем значение во втором, тогда в результирующем массиве должно быть True, иначе False

import numpy as np

def solution(arr):
    arr = arr[:, 0] > arr[:, 2]
    return arr
