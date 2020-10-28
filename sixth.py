# let us c
# Input a six digit number through the keyboard and print the sum of the digits
a = int(input("Enter six digit number, to print  the sum of digits:"))
t = 0
while a != 0:
    d = a % 10
    t = t+d
    a = a//10
print("sum of digits:", t)
