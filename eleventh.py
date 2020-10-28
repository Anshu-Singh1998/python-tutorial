# let us c
# Two numbers are entered through the keyboard . Write a program
# to find out the value of one number raised to the power of another.
m = int(input("Enter number to find out power:"))
n = int(input("Enter exponent number to find out power:"))
power = 1
i = 1
while i <= n:
    power = power * m
    i = i + 1
    print(m)
    print(n)
    print(power)
