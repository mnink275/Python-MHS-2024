import numpy as np

class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(np.add(self.data, other.data).tolist()) # type: ignore

    def __sub__(self, other):
        return self.__class__(np.subtract(self.data, other.data).tolist()) # type: ignore

    def __mul__(self, other):
        return self.__class__(np.multiply(self.data, other.data).tolist()) # type: ignore

    def __matmul__(self, other):
        return self.__class__(np.matmul(self.data, other.data).tolist()) # type: ignore

class WriteToFileMixin:
    def serialize(self, filename: str):
        with open(filename, 'w') as output:
            output.write(str(self))

class ConsoleOutputMixin:
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) + '\n' # type: ignore

    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) + '\n' # type: ignore

class GetterSetterMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data must be a list of lists")
        self._data = data

    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, rows):
        if rows <= 0:
            raise ValueError("Number of rows must be greater than 0")
        self._rows = rows

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        if cols <= 0:
            raise ValueError("Number of columns must be greater than 0")
        self._cols = cols

class Matrix(ArithmeticMixin, WriteToFileMixin, ConsoleOutputMixin, GetterSetterMixin):
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

if __name__ == '__main__':
    np.random.seed(0)

    a_data = np.random.randint(0, 10, (10, 10))
    b_data = np.random.randint(0, 10, (10, 10))

    a = Matrix(a_data.tolist())
    b = Matrix(b_data.tolist())

    path = 'hw3/artifacts/3.2/'
    (a + b).serialize(path + 'matrix+.txt')
    (a - b).serialize(path + 'matrix-.txt')
    (a * b).serialize(path + 'matrix*.txt')
    (a @ b).serialize(path + 'matrix@.txt')
