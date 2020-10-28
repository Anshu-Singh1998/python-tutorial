# let us c
# Input any year through keyboard. wap to determine whether  it is leap year or not
year = int(input("Enter a year to check whether it is leap or not:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
