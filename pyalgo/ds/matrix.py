def create(rows, cols, base=0):
    return [[base] * cols for _ in range(rows)]


def shape(matrix):
    return (len(matrix), len(matrix[0]))


def add(a, b):

    if shape(a) != shape(b):
        return None

    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def row(matrix, n):
    if shape(matrix)[0] <= n:
        return None
    return matrix[n]


def col(matrix, m):
    if shape(matrix)[1] <= m:
        return None
    return [row[m] for row in matrix]


def transcope(matrix):
    rows, cols = shape(matrix)
    t_matrix = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    return t_matrix


if __name__ == "__main__":

    m1 = create(2, 3, 1)
    m2 = create(2, 3, 2)
    m3 = [[1, 2, 3], [4, 5, 6]]
    print(m1)
    print(m2)
    print(col(m3, 0))

    print(transcope(m3))
