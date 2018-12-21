from utils import *

def LU_decomposition(matrix):
	n = len(matrix[0])
	m = len(matrix)
	l = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
	for i in range(n):
		e = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
		for j in range(i + 1, m):
			l[j][i] = matrix[j][i]/matrix[i][i]
			e[j][i] = (matrix[j][i]/matrix[i][i]) * -1
		matrix = multiple_matrix(e, matrix)
	return [l, matrix]



def solve():
	matrix = getInput()
	if matrix == False:
		print('invalid input');
	else:
		l, u = LU_decomposition(matrix)
		print_matrix(l)
		print_matrix(u)

	return

solve()
