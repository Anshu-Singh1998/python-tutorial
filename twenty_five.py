# let us c
# Any year is entered through the keyboard . Write a function to determine whether
# the year is a leap year or not.
year = int(input("Enter any year:"))


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "year entered is leap year!"
            else:
                return "Not a leap year!"
        else:
            return "Not a leap year!"
    else:
        return "Not a leap year!"


if leap_year(year):
    print("Leap year")
else:
    print("Not a leap year!")
