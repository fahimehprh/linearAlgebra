def is_matrix_valid(matrix):
	return len(matrix) != 0 and len(matrix[0]) != 0 and all([len(row) == len(matrix[0]) for row in matrix])

def is_mutiple_valid(a, b):
	return is_matrix_valid(a) and is_matrix_valid(b) and len(a[0]) == len(b)


def getInput():
	m = int(input('number of rows, m : '))
	n = int(input('number of columns, n : '))
	matrix = []

	for i in range(m):
	    matrix.append(list(map(int, input().rstrip().split())))
	return matrix if is_matrix_valid(matrix) else False

def print_matrix(matrix):
	for row in matrix:
		print(' '.join([str(int(n * 10) / 10) for n in row]))
	print()

def multiple_matrix(a, b):
	if not is_mutiple_valid(a, b):
		return False
	zip_b = list(zip(*b))
	return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]
