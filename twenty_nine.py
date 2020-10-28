# let us c
# Write a program to multiply any two 3*3 matrices
x = [[1, 8, 5],
     [2, 5, 7],
     [4, 8, 1]]
y = [[2, 8, 3],
     [5, 9, 2],
     [4, 6, 3]]
z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(y)):
        z[i][j] = x[i][j] * y[i][j]
        print(z)