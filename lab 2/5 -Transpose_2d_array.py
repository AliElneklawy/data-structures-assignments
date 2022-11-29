from json import loads

matrix = loads(input())
arr_len = len(matrix[0])
mat_len = len(matrix)

if arr_len == 0:
    print([[]])
else:
    transpose = [[0 for _ in range(mat_len)] for _ in range(arr_len)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    print(transpose)