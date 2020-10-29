# let us c
# Write a program to generate all combinations of 1, 2 nd 3 using loop.
def comb(a):
    for i in range(3):
        for j in range(3):
            for k in range(3):

                if i != j and j != k and i != k:
                    print(a[i], a[j], a[k])


comb([1, 2, 3])
