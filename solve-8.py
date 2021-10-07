from sys import stdin
from copy import deepcopy


class Matrix:
    body = []

    def __init__(self, body=[]):
        self.body = []
        for i in body:
            self.body.append(i[:])

    def __str__(self):
        result = ''
        for i in self.body:
            for j in i:
                result += str(j) + '\t'
            result = result[:-1]
            result += '\n'
        result = result[:-1]
        return result

    def size(self):
        return (len(self.body), len(self.body[0]))

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        result = deepcopy(self.body)
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                result[i][j] += other.body[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = Matrix(list(map(lambda x:
                                     list(map(lambda y: y * other, x)),
                                     self.body)))
            return result
        elif type(other) == type(self):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            result = [[0] * other.size()[1] for _ in range(self.size()[0])]
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    x = 0
                    for a in range(self.size()[1]):
                        x += self.body[i][a] * other.body[a][j]
                    result[i][j] = x
            return type(self)(result)

    def __rmul__(self, other):
        return self * other

    def transpose(self):
        result = [[0]*self.size()[0] for _ in range(self.size()[1])]
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                result[j][i] = self.body[i][j]
        self.body = result
        return Matrix(result)

    @staticmethod
    def transposed(self):
        result = [[0] * self.size()[0] for _ in range(self.size()[1])]
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                result[j][i] = self.body[i][j]
        return Matrix(result)


class SquareMatrix(Matrix):
    def __pow__(self, power):
        if power == 0:
            answer_array = [[0] * self.size()[0]
                            for _ in range(self.size()[0])]
            for i in range(len(answer_array)):
                answer_array[i][i] = 1
            return Matrix(answer_array)
        if power == 1:
            return self
        if power % 2 == 0:
            preans = self**(power // 2)
            return preans * preans
        if power % 2 == 1:
            preans = self ** (power // 2)
            return (preans * preans * self)


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


# Task 6 check 3
m = SquareMatrix([[1, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1]]
                )
print(m)
print('----------')
print(m ** 1)
print('----------')
print(m ** 2)
print('----------')
print(m ** 3)
print('----------')
print(m ** 4)
print('----------')
print(m ** 5)

#exec(stdin.read())
