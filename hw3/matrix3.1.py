import numpy as np

class Matrix:
    def __init__(self, cols = None, rows = None, data = None):
        if data is not None:
            if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
                raise TypeError("Data must be a list of lists")

            self._rows = len(data)
            self._cols = len(data[0])
            self._data = data
        elif cols is not None and rows is not None:
            self._rows = rows
            self._cols = cols
            self._data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            raise ValueError("Either data or rows and cols must be provided")

    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self._data]) + '\n'

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Matrices must have the same dimensions")

        result = Matrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                result._data[i][j] = self._data[i][j] + other._data[i][j]

        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Matrices must have the same dimensions")

        result = Matrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                result._data[i][j] = self._data[i][j] * other._data[i][j]

        return result

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self._cols != other._rows:
            raise ValueError("Number of columns in the left matrix must be equal to the number of rows in the right matrix")

        result = Matrix(self._rows, other._cols)
        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(self._cols):
                    result._data[i][j] += self._data[i][k] * other._data[k][j]

        return result

if __name__ == '__main__':
    np.random.seed(0)

    a_data = np.random.randint(0, 10, (10, 10))
    b_data = np.random.randint(0, 10, (10, 10))

    a = Matrix(data=a_data.tolist())
    b = Matrix(data=b_data.tolist())

    path = 'hw3/artifacts/3.1/'
    with open(path + 'matrix+.txt', 'w') as output:
        output.write(str(a + b))

    with open(path + 'matrix*.txt', 'w') as output:
        output.write(str(a * b))
    
    with open(path + 'matrix@.txt', 'w') as output:
        output.write(str(a @ b))
