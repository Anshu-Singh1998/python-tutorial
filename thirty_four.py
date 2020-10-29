# let us c
# Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate
# of Rs.12.00 per hour for every hour worked 40 hours. Assume that employees do not work
# for fractional part of an hour.
hours = int(input("Enter hours for employee is working:"))
employee = 1
for i in range(employee, 10):
    print(employee)
    employee = employee + 1
    print("The number number of hours employee worked:")
    if hours > 40:
        over_time = hours - 40
        over_pay = over_time * 12
        print("overtime paid to employee is", over_pay)
    else:
        print("Employee hasn't worked for over time")
