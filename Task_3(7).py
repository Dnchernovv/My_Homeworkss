class Cell:
    def __init__(self,c_num):
        self.c_num = c_num
        self.return_cell()
        self.cell_def = ''
    def return_cell(self):
        self.cell_def = '*' * self.c_num
        return self.cell_def
    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.c_num // rows)]) + '\n' + '*' * (self.c_num % rows)
    def __add__(self, other):
        return self.c_num + other
    def __sub__(self, other):
        return self.c_num - other
    def __mul__(self, other):
        return self.c_num * other
    def __truediv__(self, other):
        return round(self.c_num/other)

cll = Cell(14)
print(cll.return_cell())
print(cll.make_order(5))