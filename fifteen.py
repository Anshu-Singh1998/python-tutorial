# let us c
# Write a function which recieves 2 integers and returns the sum and average.
def sum(x, y):
    return x + y


def avg(x, y):
    return sum(x, y) // 2


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Sum of the given two numbers is: ", sum(a, b))
print("Average of the given numbers is: ", avg(a, b))
