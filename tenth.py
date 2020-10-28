# let us c
# write a program to find out the factorial value of any number entered through
# the keyboard.
a = int(input("Enter a number to find out its factorial:"))
factorial = 1
n = 1
while n <= a:
    factorial = factorial * n
    n = n + 1
print("Factorial of a number", a, "is", factorial)
