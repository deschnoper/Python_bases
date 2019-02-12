# [Андрей Гурьянов]

'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

# К сожалению, сложение матриц реализовать так и не удалось... :-(


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    #@staticmethod
    def __add__(self, mtrx):
        self.mtrx = mtrx
        #for i, line in enumerate(self.lst):
        #    for j, el in enumerate(line):
        #        result = self.lst[i][j].__add__(self.mtrx[i][j])
        return self.lst.__add__(self.mtrx) #result

    def __str__(self):
        for line in self.lst:
            print(line)
        return ''



matrix_1 = Matrix([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
