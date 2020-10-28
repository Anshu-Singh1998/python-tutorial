# let us c
# A five digit number is entered through the keyboard . Write a program to obtain the reversed
# number and to determine whether the original and reversed numbers are equal or not.
num = int(input("Enter a five digit number:",))
x = 0
print("The number to be reversed:", num)
e = num % 10
d = (num/10) % 10
c = (num/100) % 10
b = (num/1000) % 10
a = (num/100000) % 10
x = e*100000 + d*10000 + c*1000 + b*100 + a*10
print((x))
if x == num:
    print("Number got reversed", num)
else:
    print("Number is not reversed", num)
