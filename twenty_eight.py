# let us c
# Write a program to add two 4*4 matrices.
x = [[1, 2, 3, 0],
     [4, 5, 6, 5],
     [7, 8, 9, 6],
     [3, 6, 4, 2]]
y = [[1, 5, 7, 9],
     [5, 8, 2, 0],
     [4, 0, 6, 1],
     [4, 6, 9, 10]]
z = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
for i in range(len(x)):
    for j in range(len(y)):
        z[i][j] = x[i][j] + y[i][j]
        print(z)
