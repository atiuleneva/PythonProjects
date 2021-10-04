from abc import ABC, abstractmethod
print("Task #1")


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ""
        for el_list in self.matrix:
            for el_num in el_list:
                str_matrix += f'{el_num}   '
            str_matrix += "\n"

        return str_matrix

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_sum.append(line)

        return Matrix(matrix_sum)


matrix_a = Matrix([
    [1, 2, 3],
    [3, 2, 1],
    [2, 3, 1]
])
print(matrix_a)

matrix_b = Matrix([
    [4, 5, 6],
    [6, 5, 4],
    [5, 6, 4]
])
print(matrix_b)

matrix_c = matrix_a + matrix_b
print(matrix_c)


print("Task #2")


class Clothes(ABC):
    def __init__(self, param):
        self.param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calculate(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculate(self):
        return self.h*2 + 0.3


coat_1 = Coat(44)
print(coat_1.calculate)

suit_1 = Suit(175)
print(suit_1.calculate)


print("Task #3")


class CellException(Exception):
    pass


class Cell:

    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        result = self.num_cells - other.num_cells
        if result < 0:
            raise CellException("Невозможно выполнить операцию вычитания клеток")

        return Cell(result)

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        return Cell(int(self.num_cells / other.num_cells))

    def make_order(self, cells_per_row):
        out_str = ""
        for c in range(1, self.num_cells + 1):
            out_str += "*"
            if c % cells_per_row == 0:
                out_str += "\n "

        return out_str


cell1 = Cell(9)
cell2 = Cell(8)
cell3 = Cell(5)
cell4 = Cell(11)

cell_math = cell1 + cell2
print(f'cell1 + cell2 = \n {cell_math.make_order(5)}')

cell_math = cell2 - cell3
print(f'cell2 - cell3 = \n {cell_math.make_order(5)}')

cell_math = cell3 * cell4
print(f'cell3 * cell4 = \n {cell_math.make_order(11)}')

cell_math = cell4 / cell3
print(f'cell4 / cell3 = \n {cell_math.make_order(1)}')

try:
    call_math = cell3 - cell4
except CellException:
    print('Невозможно выполнить операцию вычитания клеток')