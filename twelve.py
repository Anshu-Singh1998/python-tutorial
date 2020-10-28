# let us c
# Write a program to print out a armstrong number between 1 to 500.
a = int(input("Enter 1st number print armstrong number between two numbers: "))
b = int(input("Enter 2nd number to print armstrong number between two numbers: "))

for num in range(a, b + 1):
    s = 0
    temporary = num
    while temporary > 0:
        digit = temporary % 10
        s += digit ** 3
        temporary //= 10
        if num == s:
            print(num)
