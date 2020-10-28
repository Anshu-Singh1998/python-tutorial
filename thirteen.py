# let us c
# write a program number to print all the prime numbers between 1 to 100.

num1 = int(input(" Please Enter the first given Value: "))
num2 = int(input(" Please Enter the second given  Value: "))

Number = num1

while Number <= num2:
    count = 0
    i = 2

    while i <= Number // 2:
        if Number % i == 0:
            count = count + 1
            break
        i = i + 1

    if count == 0 and Number != 1:
        print(Number, end='  ')
    Number = Number + 1
