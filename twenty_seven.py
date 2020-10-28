# let us c
# A five digit number is entered through the keyboard, write a function to calculate
# sum of digits of the 5 digit number.

def Sum_Of_Digits(Num):
    Sum = 0
    while Num > 0:
        a = Num % 10
        Sum = Sum + a
        Num = Num // 10
    return Sum


Num = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Num)
print(Sum)
