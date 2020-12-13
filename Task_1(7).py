from operator import add

class Matrix:
    def __init__(self,mat):
        self.mat = mat
        self.prep = [str(i) for i in self.mat]
        self.view = '\n'.join(self.prep)
        self.check()
    def __str__(self):
        return f'{self.view}'
    def check(self):
        for i in range(1,len(self.mat)):
            if len(self.mat[i]) == len(self.mat[i-1]):
                print('String looks fine')
            else:
                print('Please,remember how the matrixes look')
                raise ValueError
    def __add__(self, other):
        answer = ''
        if len(self.mat) == len(other.mat):
            for line_1, line_2 in zip(self.mat, other.mat):
                if len(line_1) != len(line_2):
                        return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer

matr_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matr_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matr_1 + matr_2)
