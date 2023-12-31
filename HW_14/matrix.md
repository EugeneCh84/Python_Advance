Класс Matrix. Обеспечивает функционал:

вывода на печать
сравнения
сложения
умножения матриц
Для использования матричных вычислений необходимо подключить модуль:

>>> from matrixses.matrix_class import Matrix
Для проверки тестовых случаев создадим матрицы

>>> matrix_1 = Matrix(matrix=[[2, 3, 8], [4, 6, 9], [5, 7, 1]])
>>> matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
Выведем матрицу 1 на экран:

>>> print(matrix_1)
  2   3   8 
  4   6   9 
  5   7   1 
<BLANKLINE>
Выведем матрицу 2 на экран:

>>> print(matrix_2)
  4   2   8 
  7   1   5 
  2   8   3 
<BLANKLINE>
Получим мтрицу 3 как рдезультат сложения первых двух матриц:

>>> matrix_3 = matrix_1 + matrix_2
>>> print(matrix_3)
  6   5  16 
 11   7  14 
  7  15   4 
<BLANKLINE>
Пример вычитания матриц:

>>> matrix_4 = matrix_1 - matrix_2
>>> print(matrix_4)
 -2   1   0 
 -3   5   4 
  3  -1  -2 
<BLANKLINE>
Сравним матрицу 1 саму с собой:

>>> print(matrix_1 == matrix_1)
True
Сравним две различные матрицы:

>>> print(matrix_1 == matrix_2)
False
Создадим дополнительно уще три матрицы 5, 6, 7:

>>> matrix_5 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
>>> matrix_6 = Matrix(matrix=[[4, 8], [1, 5], [2, 3]])
>>> matrix_7 = Matrix(matrix=[[4, 2, 8], [7, 1, 5]])
Умножим матрицу 1 на матрицу 5:

>>> print(matrix_1 * matrix_5)
 64  40  24 
 72  45  27 
  8   5   3 
<BLANKLINE>
Умножим матрицу 1 на матрицу 6:

>>> print(matrix_1 * matrix_6)
 24  15 
 48  30 
 56  35 
<BLANKLINE>