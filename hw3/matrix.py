import numpy as np

class Matrix:
    def __init__(self, cols = None, rows = None, data = None):
        if data is not None:
            if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
                raise TypeError("Data must be a list of lists")

            self.rows = len(data)
            self.cols = len(data[0])
            self.data = data
        elif cols is not None and rows is not None:
            self.rows = rows
            self.cols = cols
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            raise ValueError("Either data or rows and cols must be provided")

    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) + '\n'

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * other.data[i][j]

        return result

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError("Number of columns in the left matrix must be equal to the number of rows in the right matrix")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

if __name__ == '__main__':
    np.random.seed(0)

    a_data = np.random.randint(0, 10, (10, 10))
    b_data = np.random.randint(0, 10, (10, 10))

    a = Matrix(data=a_data.tolist())
    b = Matrix(data=b_data.tolist())

    path = 'hw3/artifacts/3.1/'
    with open(path + 'matrix+.txt', 'w+') as output:
        output.write(str(a + b))

    with open(path + 'matrix*.txt', 'w+') as output:
        output.write(str(a * b))
    
    with open(path + 'matrix@.txt', 'w+') as output:
        output.write(str(a @ b))
