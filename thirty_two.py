# let us c
# Any year is entered through the keyboard, write a program to determine whether
# the year is leap or not. Use the logical operator.
year = int(input("Enter a year through keyboard:"))
if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("This is leap year!")
    else:
        ("Not a leap year!")
else:
    print("Not a leap year!!!!")
