# let us c
# Write a function to calculate the factorial value of any integer enyered
# through the keyboard.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Input a number to compute the factorial : "))
print(factorial(n))
