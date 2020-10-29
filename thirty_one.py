# let us c
# According to the Gregorian calendar , it was monday on the date 01/01/190. If any year
# is input through the keyboard. Write a program to find out what is the day on 1st
# january of this year.
bas_year = 1900
year = int(input("Enter any year:"))
year = (year - 1) - bas_year
leap_year = year / 4
remaining_year = year - leap_year
total_days = (remaining_year * 365) + (leap_year * 366) + 1
days = (total_days % 7)
print(days)
if days == 0:
    print("Monday")
elif days == 1:
    print("Tuesday")
elif days == 2:
    print("Wednesday")
elif days == 3:
    print("Thursday")
elif days == 4:
    print("Friday")
elif days == 5:
    print("Saturday")
elif days == 6:
    print("Sunday")
else:
    print("Wrong met")
