A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 1, 1], [2, 2, 2]]
C = [[0]*3 for i in range(2)]
for i in range(2):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j], " ", end="")
    print()
